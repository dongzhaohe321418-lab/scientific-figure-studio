#!/usr/bin/env python3
"""Conservative SVG structure audit; does not judge science or appearance."""
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def audit(path, full_vector=False, live_text=False):
    errors = []
    warnings = []
    raw = Path(path).read_text(encoding="utf-8-sig")
    if re.search(r"<!\s*(DOCTYPE|ENTITY)\b", raw, re.I):
        return {"errors": ["DTD/entity declarations are unsupported"], "warnings": []}
    root = ET.fromstring(raw)
    tag = lambda node: node.tag.rsplit("}", 1)[-1]
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        errors.append("Root must be an SVG element in the SVG namespace")
    nodes = list(root.iter())
    counts = {name: sum(tag(n) == name for n in nodes)
              for name in ("image", "text", "path", "g", "foreignObject", "feImage")}
    geometry = sum(tag(n) in {"path", "rect", "circle", "ellipse", "line", "polyline", "polygon", "use"}
                   for n in nodes)
    texts = ["".join(n.itertext()).strip() for n in nodes if tag(n) == "text"]
    ids = [n.attrib["id"] for n in nodes if "id" in n.attrib]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate IDs make references or editing ambiguous")
    if not geometry:
        warnings.append("No conventional vector geometry found")
    if live_text and not any(texts):
        errors.append("No non-empty live text elements found")
    if full_vector and (counts["image"] or counts["feImage"] or counts["foreignObject"]):
        errors.append("Full-vector mode excludes image, feImage and foreignObject elements")
    if full_vector and not geometry:
        errors.append("Full-vector mode requires vector geometry")
    for n in nodes:
        if tag(n) == "script" or any(k.lower().startswith("on") for k in n.attrib):
            errors.append("Active script/event content is unsupported")
        for k, value in n.attrib.items():
            if k.rsplit("}", 1)[-1] == "href" and value and not value.startswith(("#", "data:")):
                errors.append("External href dependency: " + value)
        if tag(n) == "style":
            warnings.append("CSS styling requires renderer/editor inspection")
    # Find URL dependencies in presentation attributes and styles too.
    for match in re.finditer(r"url\(\s*(['\"]?)(.*?)\1\s*\)", raw, re.I):
        value = match.group(2).strip()
        if not value.startswith("#"):
            errors.append("Non-fragment CSS URL requires explicit handling")
    if re.search(r"@import\b", raw, re.I):
        errors.append("CSS imports prevent a self-contained SVG")
    if full_vector and re.search(r"data:image/", raw, re.I):
        errors.append("Embedded image data is incompatible with this full-vector audit")
    if not any(tag(n) == "g" and n.get("id") for n in nodes):
        warnings.append("No named groups found; inspect semantic grouping")
    return {"counts": counts, "geometry_elements": geometry, "live_labels": texts,
            "errors": sorted(set(errors)), "warnings": sorted(set(warnings)),
            "scope": "Structural checks only; rendering, semantic editing, science and aesthetics need inspection."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("svg", type=Path)
    p.add_argument("--full-vector", action="store_true")
    p.add_argument("--live-text", action="store_true")
    args = p.parse_args()
    try:
        result = audit(args.svg, args.full_vector, args.live_text)
    except (OSError, UnicodeError, ET.ParseError) as exc:
        result = {"errors": [str(exc)], "warnings": []}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
