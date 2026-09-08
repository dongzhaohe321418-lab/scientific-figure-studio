# Validation status

This file separates tooling checks from actual figure-production evidence.

## Release checks

- Checked on 8 September 2026, Windows, Python 3.12.
- Python regression suite: **37 tests passed**, using `python -m unittest discover -s tests -v`. The original 26 tooling tests are joined by 11 example-invariant/mutation tests: four canonical cases plus deliberate atom, charge, arrow, screen, head and graph errors.
- Codex skill metadata validation: **passed** using the installed official `skill-creator/scripts/quick_validate.py` (PyYAML was required by that external validator, not by this repository's scripts).
- Relative documentation links: all resolved in the test suite.
- Blank review template: **correctly rejected** with exit code 1 by `python scripts/check_release.py assets/review-template.json`.
- Six example review records passed the release checker with matching evidence hashes and final SVG structural checks. This is evidence bookkeeping, not independent scientific certification.
- Behavioural scenarios beyond the six named cases remain proposed evaluations; they are not automatically executed by the unit tests.

## Live biology case in v0.2.0

The [clathrin-mediated endocytosis example](examples/biology-endocytosis/README.md) includes primary-source research, inspection of two published figures, two actual native image-generation calls, inspection and correction of generated defects, original semantic SVG reconstruction, and a PNG exported from that SVG. The final PNG was decoded and visually inspected at original resolution, beyond the release checker's limited PNG header test.

- Final PNG: **3840 × 2080 pixels**.
- Final SVG: **68 selectable semantic objects**, including 24 live text elements and 44 named component groups; no raster images or external resources. The structural audit returned no errors or warnings.
- Real editor test: import a local SVG, modify a label, recolour a component, move an arrow, download the edited SVG, reload the editor, reopen that saved file and verify retained edits. Export and inspect a PNG from the reopened SVG. The saved test copies and actual observations are included in the example.
- Editor environment: bundled self-contained HTML editor served on a loopback-only HTTP server in the Codex Chromium browser. Direct `file://` navigation was blocked by the browser's URL policy; no bypass was attempted. Direct double-click HTML opening, Inkscape, Illustrator and PowerPoint were **not tested**.
- Native model provenance: requested image2 workflow; the tool exposes no model selector or quality parameter and does not report its exact backend. No verified-highest-version claim is made.

## Limits of the evidence

Scientific and aesthetic review was performed by the executing agent, not an independent expert. The six conceptual cases do not prove journal acceptance, atomic structural fidelity or whole-discipline performance. Untested specialities retain procedural guidance only. Regression tests establish only their selected deterministic properties; mutated fixtures are deliberately synthetic errors, not additional live generation trials.

## Added live cases in v0.3.0

| Case | Final PNG | Semantic objects | Real local editor round trip |
| --- | --- | --- | --- |
| [4–5–5–3 neural network](examples/neural-network/README.md) | 4800 × 2800 | 188 | Passed |
| [Methyl SN2](examples/cross-discipline/chemistry-sn2/README.md) | 4000 × 2400 | 95 | Passed |
| [Confined aquifer](examples/cross-discipline/earth-confined-aquifer/README.md) | 4000 × 2400 | 30 | Passed |
| [Terrestrial carbon pathways](examples/cross-discipline/ecology-carbon/README.md) | 4000 × 2400 | 51 | Passed |
| [Causal DAG motifs](examples/cross-discipline/research-causal-dags/README.md) | 4000 × 2400 | 57 | Passed |

The four-case set involved seven actual native calls: four initial generations, two chemical corrections and one groundwater correction. The neural-network case used one native call. Failed raster versions and the precise changes are recorded; they are not final deliverables. The initial chemistry and groundwater defects make clear why generation alone is insufficient. Actual output PNGs and saved editor exports were fully decoded and visually inspected.

All four new editor tests changed a label, component colour and arrow position; downloaded the SVG; reloaded the page; reimported the saved file; checked retained edits; exported and inspected PNG. The same loopback browser environment and untested desktop/file-URL limitations apply. Gradient recolouring now uses opaque colour tints so underlying diagram lines do not show through previously opaque nodes. The fix was exercised in the neural-network and cross-discipline UI tests.

Read the [case-specific protocol, observed defects and limits](references/cross-discipline-evaluation.md). No exact native backend snapshot, highest-model selection, independent peer review or publisher-size preflight is claimed.

The workflow requires actual figure inspection when used. A release record is evidence bookkeeping, not a certificate that its author was truthful. The SVG auditor is conservative and incomplete; it cannot infer semantic grouping, render CSS fully, or prove that every visible label is live text. Inspect the target editor and final output.
