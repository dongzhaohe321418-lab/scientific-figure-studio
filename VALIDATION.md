# Validation status

This file separates tooling checks from actual figure-production evidence.

## Release checks

- Checked on 8 September 2026, Windows, Python 3.12.
- Python regression suite: **23 tests passed**, using `python -m unittest discover -s tests -v`.
- Codex skill metadata validation: **passed** using the installed official `skill-creator/scripts/quick_validate.py` (PyYAML was required by that external validator, not by this repository's scripts).
- Relative documentation links: all resolved in the test suite.
- Blank review template: **correctly rejected** with exit code 1 by `python scripts/check_release.py assets/review-template.json`.
- Behavioural scenarios: provided for future live evaluation; they are not automatically executed by the unit tests.

## What has not been demonstrated by these checks

No new live image2 generation, full editable reconstruction, target-editor round trip, independent scientific review or journal acceptance evaluation was performed as part of packaging this initial skill. The tests use explicitly synthetic fixtures. Passing them proves only their stated deterministic properties.

The workflow requires actual figure inspection when used. A release record is evidence bookkeeping, not a certificate that its author was truthful. The SVG auditor is conservative and incomplete; it cannot infer semantic grouping, render CSS fully, or prove that every visible label is live text. Inspect the target editor and final output.
