#!/usr/bin/env python3
"""Build a colour-region component demo, not a scientific model or converter."""
import argparse
import copy
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from fit_svg_region import element, fit_region, write_svg


def build(source):
    region, _ = fit_region(source, columns=55, rows=43, prefix="field-colours")
    root = element("svg", width=760, height=360, viewBox="0 0 760 360")
    root.append(element("title")); root[-1].text = "Editable region integration demo"
    root.append(element("desc"))
    root[-1].text = "Illustrative colour artwork and independently editable labels, border, arrow and geometry. No measured data or scientific mechanism is represented."
    root.append(element("rect", width=760, height=360, fill="white"))
    for label, x, y, value, size in [
        ("heading", 36, 38, "Colour fitting + semantic objects", 25),
        ("field-label", 36, 292, "Illustrative field", 20),
        ("component-label", 506, 246, "Vector geometry", 20),
        ("scope-label", 36, 331, "Live text, separate arrow and borders; no embedded raster.", 16),
    ]:
        node = element("text", id=label, x=x, y=y, fill="#243b4b",
                       font_family="Arial, Helvetica, sans-serif", font_size=size,
                       data_editable="true")
        node.text = value
        root.append(node)
    wrapper = element("g", transform="translate(36 62) scale(1.9)")
    wrapper.append(copy.deepcopy(region.find("{http://www.w3.org/2000/svg}g")))
    root.append(wrapper)
    frame = element("g", id="field-boundary", data_editable="true")
    frame.append(element("rect", x=36, y=62, width=258.4, height=201.4,
                         fill="none", stroke="#426c84", stroke_width=1.5))
    root.append(frame)
    arrow = element("g", id="connection-arrow", data_editable="true")
    arrow.append(element("path", d="M 337 168 H 454", fill="none",
                         stroke="#426c84", stroke_width=2.5))
    arrow.append(element("path", d="M 454 168 L 444 162 L 444 174 Z", fill="#426c84"))
    root.append(arrow)
    component = element("g", id="vector-component", data_editable="true")
    component.append(element("rect", x=510, y=126, width=140, height=84,
                             fill="#dceaf0", stroke="#426c84", stroke_width=1.5))
    root.append(component)
    return region, root


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Directory for new SVG files")
    args = parser.parse_args()
    targets = [args.output / name for name in ("region.svg", "example.svg")]
    if any(path.exists() for path in targets):
        parser.error("Choose a directory without existing region.svg or example.svg")
    args.output.mkdir(parents=True, exist_ok=True)
    for root, target in zip(build(Path(__file__).with_name("source.png")), targets):
        write_svg(root, target)
        print(target.name)


if __name__ == "__main__":
    main()
