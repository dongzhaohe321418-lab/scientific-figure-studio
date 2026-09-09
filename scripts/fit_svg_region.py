#!/usr/bin/env python3
"""Approximate an opaque PNG colour region with editable SVG gradients.

This is a texture-region helper, not an OCR, diagram parser or whole-figure
converter. Keep scientific geometry and live labels in a separate semantic
reconstruction. Requires Pillow only; importing this module does not require it.
"""
import argparse
import hashlib
import io
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def element(name, **attrs):
    return ET.Element("{" + NS + "}" + name,
                      {key.replace("_", "-"): str(value) for key, value in attrs.items()})


def sample_rgb(image, x, y):
    """Bilinear sampling of an RGB Pillow image, with endpoints clamped."""
    x = max(0, min(image.width - 1, x))
    y = max(0, min(image.height - 1, y))
    x0, y0 = math.floor(x), math.floor(y)
    x1, y1 = min(x0 + 1, image.width - 1), min(y0 + 1, image.height - 1)
    u, v = x - x0, y - y0
    pixels = [image.getpixel(p) for p in [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]]
    weights = [(1-u)*(1-v), u*(1-v), (1-u)*v, u*v]
    return tuple(round(sum(w * p[c] for w, p in zip(weights, pixels))) for c in range(3))


def fit_region(source, crop=None, columns=27, rows=21, prefix="colour-region"):
    """Return an SVG root and provenance without changing the source image."""
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.-]*", prefix):
        raise ValueError("id prefix must be an ASCII XML identifier without a colon")
    if any(type(n) is not int or not 2 <= n <= 256 for n in (columns, rows)):
        raise ValueError("columns and rows must be integers from 2 to 256")
    try:
        from PIL import Image
    except ImportError as exc:
        raise ValueError("Install the optional dependency: python -m pip install Pillow") from exc
    source = Path(source)
    raw = source.read_bytes()
    with Image.open(io.BytesIO(raw)) as opened:
        if opened.format != "PNG":
            raise ValueError("Input must be an actual PNG")
        width, height = opened.size
        crop = tuple(crop) if crop is not None else (0, 0, width, height)
        if len(crop) != 4 or any(type(n) is not int for n in crop):
            raise ValueError("crop must contain four integers: x y width height")
        x, y, w, h = crop
        if x < 0 or y < 0 or w < 1 or h < 1 or x+w > width or y+h > height:
            raise ValueError("crop must be non-empty and inside the PNG")
        region = opened.convert("RGBA").crop((x, y, x+w, y+h))
        if region.getchannel("A").getextrema() != (255, 255):
            raise ValueError("Transparent regions are unsupported; do not silently flatten them")
        if opened.info.get("icc_profile"):
            try:
                from PIL import ImageCms
                region = ImageCms.profileToProfile(region.convert("RGB"),
                    ImageCms.ImageCmsProfile(io.BytesIO(opened.info["icc_profile"])),
                    ImageCms.createProfile("sRGB"), outputMode="RGB")
            except Exception as exc:
                raise ValueError("Could not convert the embedded ICC profile to sRGB") from exc
            colour_space = "embedded ICC profile converted to sRGB"
        else:
            if "gamma" in opened.info and "srgb" not in opened.info and abs(opened.info["gamma"] - .45455) > .005:
                raise ValueError("Non-sRGB PNG gamma requires explicit colour conversion first")
            region = region.convert("RGB")
            colour_space = "sRGB tag or untagged channels interpreted as sRGB"
    record = {
        "method": "semantic reconstruction companion: bilinear SVG colour gradients",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "source_dimensions": [width, height], "crop_xywh": list(crop),
        "grid": [columns, rows], "colour_space": colour_space,
        "scope": "Approximate colour artwork only; no recovered labels, topology or measured data.",
    }
    root = element("svg", width=w, height=h, viewBox=f"0 0 {w} {h}")
    root.append(element("title"))
    root[-1].text = "Editable approximation of a PNG colour region"
    root.append(element("desc"))
    root[-1].text = record["scope"]
    root.append(element("metadata"))
    root[-1].text = json.dumps(record, sort_keys=True)
    group = element("g", id=prefix, data_editable="true",
                    data_role="colour-region", transform=f"scale({w/100:g} {h/100:g})")
    step = 100/(rows-1)
    band_height = step + min(.5, step*.1)
    defs = element("defs")
    # Finish interpolation at the next sample row, not the overlapping edge.
    # Otherwise adjacent rows restart at slightly different colours.
    fade = element("linearGradient", id=prefix+"-fade", x1=0, y1=0, x2=0,
                   y2=f"{step/band_height:.10f}")
    fade.append(element("stop", offset=0, stop_color="white", stop_opacity=1))
    fade.append(element("stop", offset=1, stop_color="white", stop_opacity=0))
    defs.append(fade)
    mask = element("mask", id=prefix+"-mix", maskUnits="objectBoundingBox",
                   maskContentUnits="objectBoundingBox", x=0, y=0, width=1, height=1,
                   mask_type="alpha")
    mask.append(element("rect", width=1, height=1, fill=f"url(#{prefix}-fade)"))
    defs.append(mask)
    clip = element("clipPath", id=prefix+"-clip")
    clip.append(element("rect", width=100, height=100))
    defs.append(clip)
    for j in range(rows):
        gradient = element("linearGradient", id=f"{prefix}-row-{j}",
                           x1=0, y1=0, x2=1, y2=0, color_interpolation="sRGB")
        for i in range(columns):
            rgb = sample_rgb(region, (w-1)*i/(columns-1), (h-1)*j/(rows-1))
            gradient.append(element("stop", offset=f"{i/(columns-1):.8f}",
                                    stop_color="#"+"".join(f"{c:02x}" for c in rgb)))
        defs.append(gradient)
    group.append(defs)
    paint = element("g", clip_path=f"url(#{prefix}-clip)")
    paint.append(element("rect", width=100, height=100, fill=f"url(#{prefix}-row-0)"))
    # Opaque base + overlapping bands prevent transparent antialias seams.
    for j in range(rows-1):
        attrs = dict(x=0, y=f"{step*j:.8f}", width=100, height=f"{band_height:.8f}")
        paint.append(element("rect", **attrs, fill=f"url(#{prefix}-row-{j+1})"))
        paint.append(element("rect", **attrs, fill=f"url(#{prefix}-row-{j})",
                             mask=f"url(#{prefix}-mix)"))
    group.append(paint)
    root.append(group)
    return root, record


def write_svg(root, output):
    """Create a new SVG, refusing overwrite rather than risking a visual master."""
    output = Path(output)
    if output.suffix.lower() != ".svg":
        raise ValueError("Output must have an .svg extension")
    data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with output.open("xb") as stream:
        stream.write(data)
    return len(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("png", type=Path)
    parser.add_argument("svg", type=Path)
    parser.add_argument("--crop", nargs=4, type=int, metavar=("X", "Y", "WIDTH", "HEIGHT"))
    parser.add_argument("--columns", type=int, default=27)
    parser.add_argument("--rows", type=int, default=21)
    parser.add_argument("--id", dest="prefix", default="colour-region")
    args = parser.parse_args()
    try:
        root, record = fit_region(args.png, args.crop, args.columns, args.rows, args.prefix)
        record["svg_bytes"] = write_svg(root, args.svg)
        print(json.dumps(record, indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc)+"\n")


if __name__ == "__main__":
    main()
