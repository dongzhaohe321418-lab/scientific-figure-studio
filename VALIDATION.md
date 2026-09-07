# Validation status

This file separates tooling checks from actual figure-production evidence.

## Release checks

- Checked on 8 September 2026, Windows, Python 3.12.
- Python regression suite: **26 tests passed**, using `python -m unittest discover -s tests -v`. New checks reject default raster-only delivery, a fake PNG extension and an unexplained format exception.
- Codex skill metadata validation: **passed** using the installed official `skill-creator/scripts/quick_validate.py` (PyYAML was required by that external validator, not by this repository's scripts).
- Relative documentation links: all resolved in the test suite.
- Blank review template: **correctly rejected** with exit code 1 by `python scripts/check_release.py assets/review-template.json`.
- The [biology example release record](examples/biology-endocytosis/review.json): **passed** `python scripts/check_release.py examples/biology-endocytosis/review.json` with matching evidence hashes and the final SVG structural checks.
- Behavioural scenarios beyond the live case below remain proposed evaluations; they are not automatically executed by the unit tests.

## Live biology case in v0.2.0

The [clathrin-mediated endocytosis example](examples/biology-endocytosis/README.md) includes primary-source research, inspection of two published figures, two actual native image-generation calls, inspection and correction of generated defects, original semantic SVG reconstruction, and a PNG exported from that SVG. The final PNG was decoded and visually inspected at original resolution, beyond the release checker's limited PNG header test.

- Final PNG: **3840 × 2080 pixels**.
- Final SVG: **68 selectable semantic objects**, including 24 live text elements and 44 named component groups; no raster images or external resources. The structural audit returned no errors or warnings.
- Real editor test: import a local SVG, modify a label, recolour a component, move an arrow, download the edited SVG, reload the editor, reopen that saved file and verify retained edits. Export and inspect a PNG from the reopened SVG. The saved test copies and actual observations are included in the example.
- Editor environment: bundled self-contained HTML editor served on a loopback-only HTTP server in the Codex Chromium browser. Direct `file://` navigation was blocked by the browser's URL policy; no bypass was attempted. Direct double-click HTML opening, Inkscape, Illustrator and PowerPoint were **not tested**.
- Native model provenance: requested image2 workflow; the tool exposes no model selector or quality parameter and does not report its exact backend. No verified-highest-version claim is made.

## Limits of the evidence

Scientific and aesthetic review was performed by the executing agent, not an independent expert. This conceptual example does not prove journal acceptance, atomic structural fidelity, universal biological mechanisms or performance across all biology. The other disciplines have specialised procedural guides, but no new live image2-to-SVG evaluation in this release. The regression tests use explicitly synthetic fixtures and establish only their stated deterministic properties.

The workflow requires actual figure inspection when used. A release record is evidence bookkeeping, not a certificate that its author was truthful. The SVG auditor is conservative and incomplete; it cannot infer semantic grouping, render CSS fully, or prove that every visible label is live text. Inspect the target editor and final output.
