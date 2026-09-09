# PNG-to-SVG: preserve the image, reconstruct its meaning

The preferred method for suitable scientific diagrams is **semantic geometry + live text + regional appearance reconstruction**. In one local weather-network comparison, sampled colour gradients preserved continuous field appearance better than the tested tracing configurations. This is a case-level observation, not proof of a universally best or lossless converter.

## Protect the accepted PNG

Preserve the selected, scientifically eligible PNG and record its SHA-256. Use different paths for the SVG, its render and editing tests. Improve the SVG against this fixed target; never regenerate a weaker PNG to make the pair match. User acceptance of appearance does not replace scientific review or authorise publication. If a scientific defect is discovered, correct it and retain the version history.

## Route each region by its meaning

| Region | Preferred treatment | What must be verified |
| --- | --- | --- |
| Labels, equations, units and legends | Re-enter as verified live text; OCR can assist transcription | Symbols, subscripts, signs and font fallback; never treat OCR as authority |
| Devices, apparatus, network blocks and interfaces | Rebuild named objects using constrained geometry, curves and appropriate shading | Scientific topology, proportions, projection and occlusion |
| Arrows, bonds and connection lines | Rebuild explicit semantic connections with grouped shafts/heads | Direction, endpoint, branching and meaning |
| Continuous illustrative colour fields | Fit sampled gradients within a separate clipped vector region | Visual similarity and editability; no implied recovery of observations |
| Sharp irregular silhouettes or discrete colour areas | Trace selected regions, then simplify and regroup | Contours, holes, topology, banding and node burden |
| Measured plots/maps or molecular coordinates | Re-render from source data with the appropriate scientific tool | Actual values, coordinate system, units and uncertainty; do not manufacture data from artwork |
| Photographs or microscopy | Retain a clearly declared raster layer only within authorised hybrid scope | Provenance and precise editing limits; not a full-vector substitute |

Whole-page tracing is a diagnostic candidate, not the default final deliverable. It can outline lettering and fragment a meaningful component into hundreds of unrelated contours. Reconstruct scientific structure before investing in surface similarity.

## Optional colour-region helper

[fit_svg_region.py](../scripts/fit_svg_region.py) samples an opaque PNG rectangle and produces ordinary SVG linear gradients, stops, rectangles, masks and a clipping path. Horizontal sampled gradients are blended through overlapping vertical bands over an opaque base, reducing visible seams. This approximates colour artwork; it does not recover labels, object boundaries, topology or scientific data.

The audit tools remain standard-library Python. Only this optional helper requires Pillow:

~~~sh
python -m pip install Pillow
python scripts/fit_svg_region.py accepted.png region.svg --crop 120 80 240 160 --columns 27 --rows 21 --id field-colours
python scripts/audit_svg.py region.svg --full-vector
~~~

The crop arguments are **x, y, width, height**, in source pixels. Omit the crop to process the whole input when that input is already an isolated colour region. The example coordinates above are illustrative, not inferred from an arbitrary input. Use a unique ID prefix for every independently editable region placed in one parent SVG.

- The helper rejects invalid crops, actual non-PNG input and transparent regions. It converts an embedded ICC profile to sRGB when supported; untagged channels are interpreted as sRGB. Explicit non-sRGB gamma without a profile requires conversion first. Keep a colour-managed source when colour fidelity matters.
- Output keeps the crop's aspect ratio. The SVG metadata records source hash, dimensions, crop and grid without storing personal file paths. Existing output files are never overwritten.
- Copy the generated group, including its definitions, into the semantic SVG and position it within a wrapper group. Keep labels, scientific boundaries and connectors separate. Do not put the entire finished figure through the colour fitter.
- Increase the sampling grid only when matched renders show a useful improvement. More stops increase file size and editing burden; they cannot restore missing source detail. Sharp edges, tiny symbols and high-frequency textures require another representation.
- Dense row sampling can reveal antialiased strip seams even with valid SVG. The helper now overlaps bands by at least one source pixel, with interpolation still finishing at the next sampled row. Inspect the actual export at its intended scale; extreme downscaling or a different renderer may need another sampling choice. The optional rendered regression uses a synthetic field, not a scientific map.
- Colours are editable as gradient stops, and the region is movable as a group. Changing an individual feature inside the colour field is not equivalent to editing a recovered scientific object. Reused definitions or symbols may affect multiple instances; disclose that scope or clone definitions before independent editing.
- A simple SVG editor may support moving/recolouring groups without exposing every gradient stop or mask. Test the intended editor. Do not assume identical behaviour in browsers, Inkscape, Illustrator or PowerPoint.

The [public component example](../examples/vector-reconstruction/README.md) supplies an illustrative PNG region, a fitted SVG and an integration example with live labels. It is a component demonstration, not a validated scientific figure or an automatic full-figure converter.

## Comparison and editing protocol

If semantic reconstruction also improves typography and composition, use [editorial refinement](editorial-refinement.md) to decide whether it can supply the final PNG. Retain the native benchmark and actual generation provenance; a common SVG master is conditional on quality, not a mandatory conversion shortcut.

1. Match canvas, crop, resolution and background. Inspect the whole figure at intended use size and enlarged crops of scientific labels, arrows, interfaces and texture regions.
2. Compare geometry and appearance separately. An image-similarity score can favour a large white background while overlooking a reversed arrow. Regional pixel error is supplementary and cannot pass science or typography.
3. Record attempted methods/settings, selected output, actual visual losses, object/text counts and raster presence. Do not select by path count or file extension alone.
4. Edit a live label, a component colour and an arrow/object position in a separate copy. Save it, confirm the actual file exists, reopen that file, export and inspect its render. A download notification or button click is not proof of a saved file. If the environment blocks downloads, use an available authorised local save route or leave the application round trip pending.
5. Preserve the accepted PNG and canonical SVG during testing. Document the editor and the tested editing scope, including shared definitions and remaining appearance differences.

## Observed local comparison, 9 September 2026

The existing image2 PNG of a conceptual weather U-Net remained unchanged during comparison. The diagram's maps were illustrative colour fields, not measured weather output. Native generation did not expose a selectable backend version; no highest-version claim is made.

| Candidate | Observed result | Interpretation |
| --- | --- | --- |
| Whole-page VTracer 0.6.15, one tested configuration | 2,585 paths; no live text; damaged small labels and fine connections | Unsuitable as the final editable diagram in this trial |
| Semantic geometry/text with regional tracing | 46 live text objects; discrete colour bands remained visible | Better editing structure; still inferior continuous-field appearance |
| Semantic geometry/text with sampled regional gradients | 46 live text objects; no embedded raster; smoother continuous colours | Selected visually among these candidates; actual browser save/reopen/export completed through a local save helper |

Both tracing trials used colour mode, stacked layers, spline fitting, corner threshold 60, length threshold 4.0, maximum iterations 10, splice threshold 45 and path precision 2. Whole-page settings were speckle filter 4, colour precision 6 and layer difference 16; regional settings were 3, 7 and 12 respectively. These are recorded trial settings, not recommended universal defaults. The selected full-figure gradient regions used a 27 × 21 grid; the later public component trial separately selected denser sampling.

This was one agent-reviewed case. It does not compare every tracing parameter, prove general superiority, establish independent scientific review or verify other vector editors. DiffVG was researched but not executed. The generic helper and public component example are separately tested; do not present their tests as a repeat of the entire scientific figure evaluation. Raw user input and third-party research images are not included in this public example.

## Primary technical references

- [SVG 2 paint servers](https://www.w3.org/TR/SVG2/pservers.html): standard linear/radial gradients and stops; the helper does not depend on experimental mesh-gradient support.
- [VTracer project](https://github.com/visioncortex/vtracer) and [Python package](https://pypi.org/project/vtracer/): raster tracing candidate; evaluate output rather than assuming recovered semantics.
- [Inkscape tracing manual](https://inkscape-manuals.readthedocs.io/en/latest/tracing-an-image.html): tracing creates paths, with method-dependent results and further editing needs.
- [DiffVG research](https://people.csail.mit.edu/tzumao/diffvg/): differentiable vector rasterisation is a possible optimisation direction, not a tested production dependency here.
