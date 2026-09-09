# Validation status

This file separates tooling checks from actual figure-production evidence.

## Release checks

- Tooling checked on 9 September 2026, Windows, Python 3.12, with Pillow 12.3.0 installed for the optional colour-region helper.
- Python regression suite: **63 tests passed**, using `python -m unittest discover -s tests -v`. These include 26 original tooling tests, 11 example-invariant/mutation tests, 12 PNG-priority/legacy-schema tests and 14 colour-region tests. Without Pillow, the 14 optional helper tests are explicitly skipped, not counted as passed.
- Codex skill metadata validation: **passed** using the installed official `skill-creator/scripts/quick_validate.py` (PyYAML was required by that external validator; this repository's audit scripts do not require it).
- Relative documentation links: all resolved in the test suite.
- Blank review template: **correctly rejected** with exit code 1 by `python scripts/check_release.py assets/review-template.json`.
- Six historical schema 1 example records pass the release checker with `--allow-legacy`, matching evidence hashes and final SVG structural checks. They predate the PNG-priority policy and do not validate its quality-selection step.
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

## PNG-priority policy in v0.4.0

User feedback identified a real quality loss: full-vector reconstructions remained less visually refined than their raster masters, and requiring the primary PNG to be exported from SVG propagated that loss. The rule now protects the best scientifically correct PNG and improves SVG independently towards it. No new pictures were generated or visually re-evaluated for this policy-only change; the six earlier figure records remain historical evidence.

Schema 2 requires an explicitly selected primary PNG, its origin and selection rationale, a reviewed assertion that it was not degraded for SVG convenience, and a separately saved SVG preview with fidelity/difference evidence. Twelve synthetic regression tests check these requirements and explicit legacy handling. They do not measure aesthetics, prove the truth of a self-review, or demonstrate that future SVGs will match native image quality.

New reviews use schema 2 by default. Old schema 1 records are rejected unless `--allow-legacy` is explicitly supplied, and the CLI reports that PNG-priority records were not checked. No historic image or review was relabelled as passing the new policy.

## Regional reconstruction update, 9 September 2026

The [PNG-to-SVG guide](references/png-to-svg.md) records one local comparison of whole-page tracing, regional tracing and semantic reconstruction with sampled gradients. The last route was selected for that conceptual weather-network diagram. Its 46 live labels and actual browser save/reopen/export test do not establish field-wide performance or compatibility with untested desktop editors. The generated PNG was retained unchanged. The private project, raw user input and third-party research images are not published as part of this update.

The public [component example](examples/vector-reconstruction/README.md) contains an isolated illustrative colour field from that generated PNG, the reusable helper, semantic integration code, rendered previews and a comparison record. It is not a measured map, a scientific model or a seventh discipline evaluation. No additional image-generation call was made for this publication update.

- The helper uses standard SVG gradients, masks and clipped geometry; it refuses output overwrite and records source hash, crop, grid and colour-space treatment. Tests cover input/crop validation, profile conversion, transparency rejection, vector structure, protected files and interpolation continuity at overlapping sample bands.
- Both component SVGs passed their applicable structural audit with no warnings. The standalone field has no text by design; the integration example has four live text objects and no raster content. Both previews were decoded and visually inspected using Sharp 0.35.4 / librsvg 2.62.91.
- A 55 × 43 sampling grid was selected after matched comparison with 27 × 21. Regional RGB RMSE changed from approximately 5.120 to 3.534 on 8-bit channels, while SVG size grew from 36,041 to 131,551 bytes. These are one-region image errors, not scientific accuracy, whole-figure fidelity or general performance scores. Remaining smoothing and increased editing burden are disclosed.
- The integration example passed an actual source-level edit/save/reparse check for a live label, component colour and independent arrow position. Its edited PNG was rendered and visually inspected. This new component test did not operate an application UI; it is distinct from the earlier local full-figure browser round trip.
- The bundled editor now reports a download request rather than claiming that a file has been saved. Actual file existence and reopening are required by the workflow. The edited JavaScript was syntax-checked; a new editor UI round trip was not performed for this wording change.

The AI-style review guidance now targets observed excessive gloss, repetitive texture, oversized hierarchy and decorative containers while retaining meaningful scientific depth. These are review instructions, not an automatic detector of image provenance or a guarantee that every future output will meet the target.
