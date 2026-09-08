# Live cross-discipline evaluation: 8 September 2026

The workflow has six documented conceptual cases: the earlier endocytosis case, a 4–5–5–3 feedforward neural network, and the four-case cross-discipline set. All retain real generated masters, live-text vector reconstruction, saved PNG/SVG, sources and actual local editor round-trip evidence. Read the [validation record](../VALIDATION.md) and [four-case bundle](../examples/cross-discipline/README.md).

These are historical schema 1 cases. Subsequent feedback found that some SVGs remained visibly poorer than their raster masters. The v0.4.0 PNG-priority policy supersedes the old requirement to derive the primary PNG from SVG; these archived cases are not retrospective proof of visual parity or of the new selection policy.

## Required evaluation protocol

1. Name the specific representation and its assumptions before selecting the visual style. A domain label is not a scientific specification.
2. Define critical invariants independently of the picture: species and stoichiometry, interfaces, graph edges, source/destination and arrow meaning, measurement geometry and units as applicable.
3. Research primary sources and actually inspect relevant figures. Record which claims and visual attributes each supports; distinguish a section read from a figure viewed.
4. Generate and inspect the native master. Keep failed versions clearly labelled as evidence. Follow each targeted correction with a check for regressions elsewhere.
5. Secure the best scientifically correct PNG, then reconstruct meaningful vectors and inspect their separately saved render. Improve SVG fidelity without reducing the primary PNG standard. When constrained geometry matters, verify actual paths/coordinates as well as metadata. Report material/texture simplifications explicitly.
6. Where deterministic checks are useful, include a failing mutation: reverse an arrow, change an atom, move a screen outside its aquifer or misclassify a carbon flux. A validator that only repeats manually supplied `passed=true` assertions is not a check.
7. Test saved-file editing through actual application controls. Separate source validity, the UI round trip and scientific review in the evidence record.
8. Add the narrow case to the coverage table. Do not promote an entire discipline to “validated” because one case passed.

## What the new cases established

| Case | Selected checks | First generated draft | Final evidence |
| --- | --- | --- | --- |
| Methyl SN2 substitution | Atom/charge balance, single electron-pair arrowheads, partial bonds | Failed: two-headed arrow and representation defects; two native edits | Corrected source, render and actual editing test |
| Confined aquifer | Continuous bed, outcrop, local head, screen inside drawn aquifer | Failed: head/outcrop/inset defects; one native edit | Corrected source, render and actual editing test |
| Terrestrial carbon pathways | Nine specified carbon edges; energy separate | No critical mechanism error found in self-review; title restored in SVG | Original vector reconstruction and actual editing test |
| Confounder/mediator/collider DAGs | Exact edges, acyclicity, selected path blocking/opening | No critical topology error found in self-review | Original vector reconstruction and actual editing test |

There were seven native calls for the four cases: four initial generations and three edits. This is a selected, small evaluation; it does not estimate overall success rates. Backend model and quality controls were undisclosed. All scientific and aesthetic assessments were executing-agent self-reviews, not independent subject-expert evaluations.

## Boundaries and follow-up coverage

- The SN2 case is achiral: it does not test stereochemical inversion, organometallic coordination or orbital fidelity.
- The aquifer section is conceptual: it does not test GIS coordinates, transient flow, pumping solutions or a numerical model.
- The carbon example is qualitative: it does not test a closed budget, flux magnitudes, isotopes, taxonomic accuracy or climate predictions.
- The DAGs are selected three-node motifs: they do not test identification in arbitrary graphs, time-varying confounding, longitudinal mediation or empirical causal discovery.
- Endocytosis does not validate anatomy or all cellular mechanisms; the MLP does not validate transformers, convolution, biological neural anatomy or trained-model performance.
- Other branches retain procedural guidance only until their own recorded evaluations exist. Avoid claiming universal support, publisher compliance or “Nature-level” certification.

For later expansion, select an uncovered representation rather than another visually similar example: e.g. a sourced optical path, an anatomically constrained section, a coordinate-based crystal structure or a real data-derived map. Use the relevant specialist tool wherever exact data/geometry is central.
