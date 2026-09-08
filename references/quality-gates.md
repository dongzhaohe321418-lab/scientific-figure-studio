# Quality gates and evidence

These gates govern delivery claims. They are not a journal certification, a guarantee of agent compliance or an autonomous scientific referee. Scripts enforce selected structural checks and evidence bookkeeping; visual and scientific judgements require genuine inspection.

## Required gates

| Gate | Passing evidence | Blocking examples |
| --- | --- | --- |
| Science | Reviewed architecture, source mapping, arrow/label checks and caption | Reversed carrier flow; incompatible layers; invented measurements |
| Visual | Best eligible PNG selected independently; SVG render compared and its actual fidelity disclosed | PNG degraded for SVG convenience; falsely claiming parity; unreadable labels; material or projection errors |
| Typography | Every scientific label verified against the brief | Wrong subscript, dropped minus sign, stale generated label |
| Editability | Promised object types inspected and an editor save/reopen/export test recorded | Raster wrapper advertised as full vector; outlined text advertised as live |
| Portability | Final files, assets and fonts/fallbacks checked | Missing linked images; private absolute paths; broken exported geometry |
| Provenance | Prompt, route, actual controls and honest model disclosure recorded | “Highest model confirmed” without returned evidence; fictitious generation |

The default release is a persistent best-quality PNG plus editable SVG: `delivery: full-vector`, a primary `.png` registered as `preview`, a real `.svg` registered as `source`, and a separately named PNG registered as `svg-render`. The primary PNG need not be exported from SVG. Select it on scientific correctness and visual quality, retaining the better raster even when SVG is visibly simpler. The checker verifies file roles and PNG/IHDR headers; full decoding, scientific agreement and visual quality still require inspection.

A user-requested format exception requires `delivery_format_override: {"requested_by_user": true, "reason": "the actual request"}`. Do not set that flag for convenience. For an explicit raster-only request, editability can be not applicable with a reason. For supplied masters or explicitly direct vector requests, generation can be not applicable with a reason; PNG quality review is still required when delivering PNG. A requested exact model that cannot be verified remains unresolved.

## Review record

Copy `assets/review-template.json` into the output project. All template gates start pending. Set `delivery` to `raster`, `full-vector` or `hybrid`. Record generated output and final artefacts under `files` using unique project-relative paths, descriptive roles and actual SHA-256 hashes. Required roles are `brief`, `sources`, `prompt`, `preview`, `caption`, and `visual-comparison`; editable modes also need `source` and `edit-test`. If generation is legitimately not applicable, `prompt` is not required. `visual-comparison` can contain review notes and links to the compared images; it must describe what was actually viewed.

Each gate has `status`, `reviewer`, `notes` and `evidence` (a non-empty list of registered file paths). Allowed final statuses are `pass` and narrowly justified `not_applicable`; `pending` and `fail` keep the release incomplete. Notes identify checks and defects, not just “looks good”. Record unresolved defects in `unresolved`; any entry blocks a final claim.

### Schema 2: PNG selection and SVG comparison

- `png_quality.primary_file`: a registered PNG with role `preview`, selected as the primary deliverable.
- `png_quality.origin`: `image2`, `svg-render`, `composite` or `user-supplied`. `selection_reason` explains the actual comparison and scientific eligibility. SVG-derived output is allowed when it meets or improves the best eligible raster; automatic preference for file matching is forbidden.
- `png_quality.degraded_for_svg`: must explicitly be `false` after review. Null/pending, strings or `true` fail. This is a recorded assertion, not an automated aesthetic measurement.
- `png_quality.review_evidence`: non-empty registered evidence; describe the PNG candidates actually inspected and why the chosen version wins.
- For editable delivery, `svg_quality.render_file`: a registered `svg-render` PNG at a different path from the primary PNG, even if their bytes happen to match. This preserves their distinct roles.
- `svg_quality.fidelity_status`: `matched` or `differences-disclosed`. `differences` states the inspected scale and actual losses, or explicitly explains that none were visible. A visibly simplified SVG must not be marked matched. `review_evidence` links the real comparison notes.

Deliver a scientifically/visually reviewed PNG promptly even if SVG refinement remains pending. Report that partial status clearly and continue the requested SVG work. A useful PNG can be complete while the combined release check still fails for an unfinished SVG; never degrade the PNG to make that check pass.

Archived schema 1 records remain unchanged. The checker requires schema 2 by default. Use `--allow-legacy` only to recheck historical evidence; its output states that PNG-priority selection was not checked. Do not use this option for a new release or retrofit a passing comparison that never occurred.

For `full-vector`, register an SVG `source` and require the SVG audit to pass with live text. Other editable source formats can be described in the record, but this checker currently validates only SVG full-vector releases. Do not relabel an unsupported format to bypass the limitation.

Run:

```sh
python scripts/audit_svg.py output/figure.svg --full-vector --live-text
python scripts/check_release.py output/review.json
```

Both scripts use Python 3.10+ and the standard library. Exit code 0 means their documented checks pass; non-zero means incomplete or failed. Output explicitly states that science and aesthetics are not automatically verified. SHA-256 checks bind the record to file versions, not to the truth of its contents. A fabricated review can still deceive a bookkeeping checker and is forbidden by this skill.

## Practical release review

1. Check science against source evidence and the fixed brief. Never approve solely by familiarity with how the object usually looks.
2. Select and secure the best scientifically correct PNG; compare the independently saved SVG render with it. Never overwrite the primary PNG during SVG iteration. Recheck both after any scientific correction.
3. Perform the promised editor test in a separate copy, leaving the scientifically correct source intact. Record application and version when available.
4. Correct defects, regenerate hashes and rerun affected checks. Do not endlessly repeat checks unaffected by a change.
5. If a gate cannot pass, return the useful draft and the exact limitation. The task may be partially delivered, but the failed requirement is not complete.

## Maintaining this skill

Run the bundled unit tests and scenario reviews after changing the gates, model policy or reconstruction workflow. Unit tests do not constitute a live image2-to-vector evaluation. For a live evaluation, archive permitted prompts, generated masters, editable exports, matched comparisons and genuine gate records; disclose date, tool route and evaluator. Do not republish private user assets as examples.
