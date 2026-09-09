#!/usr/bin/env python3
"""Check the published component and save a source-level editing test copy.

This does not operate an application UI or establish scientific correctness.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from audit_svg import audit
from fit_svg_region import write_svg
from PIL import Image, ImageChops, ImageStat


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    source = base / "source.png"
    meta = json.loads((base / "provenance.json").read_text(encoding="utf-8"))
    assert hashlib.sha256(source.read_bytes()).hexdigest() == meta["source_sha256"]
    for name, live in [("region.svg", False), ("example.svg", True)]:
        result = audit(base / name, True, live)
        assert not result["errors"], result["errors"]
    with Image.open(source) as original, Image.open(base / "region-preview.png") as rendered:
        original.load(); rendered.load()
        assert original.format == rendered.format == "PNG"
        assert original.size == rendered.size == (136, 106)
        assert rendered.convert("RGBA").getchannel("A").getextrema() == (255, 255)
        stats = ImageStat.Stat(ImageChops.difference(original.convert("RGB"), rendered.convert("RGB")))
        error = {"mae_rgb_8bit": sum(stats.mean) / 3,
                 "rmse_rgb_8bit": math.sqrt(sum(n*n for n in stats.rms) / 3)}
    canonical = (base / "example.svg").read_bytes()
    root = ET.fromstring(canonical)
    nodes = {node.get("id"): node for node in root.iter() if node.get("id")}
    nodes["field-label"].text = "Edited illustrative field"
    nodes["vector-component"][0].set("fill", "#e7cf9e")
    nodes["connection-arrow"].set("transform", "translate(0 6)")
    args.output.mkdir(parents=True, exist_ok=True)
    target = args.output / "edit-test.svg"
    write_svg(root, target)
    reopened = ET.parse(target).getroot()
    saved = {node.get("id"): node for node in reopened.iter() if node.get("id")}
    assert saved["field-label"].text == "Edited illustrative field"
    assert saved["vector-component"][0].get("fill") == "#e7cf9e"
    assert saved["connection-arrow"].get("transform") == "translate(0 6)"
    assert (base / "example.svg").read_bytes() == canonical
    assert not audit(target, True, True)["errors"]
    print(json.dumps({"source_level_edit_save_reparse": "pass",
                      "application_ui_round_trip": "not tested by this script",
                      "region_pixel_error": error,
                      "metric_scope": "Matched illustrative colour region only; not science, text or whole-figure quality."}, indent=2))


if __name__ == "__main__":
    main()
