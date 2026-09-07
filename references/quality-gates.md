# Quality gates and evidence

These gates govern delivery claims. They are not a journal certification, a guarantee of agent compliance or an autonomous scientific referee. Scripts enforce selected structural checks and evidence bookkeeping; visual and scientific judgements require genuine inspection.

## Required gates

| Gate | Passing evidence | Blocking examples |
| --- | --- | --- |
| Science | Reviewed architecture, source mapping, arrow/label checks and caption | Reversed carrier flow; incompatible layers; invented measurements |
| Visual | Actual final render inspected at full, publication and detail scales | Generic reconstruction below benchmark; unreadable labels; material or projection errors |
| Typography | Every scientific label verified against the brief | Wrong subscript, dropped minus sign, stale generated label |
| Editability | Promised object types inspected and an editor save/reopen/export test recorded | Raster wrapper advertised as full vector; outlined text advertised as live |
| Portability | Final files, assets and fonts/fallbacks checked | Missing linked images; private absolute paths; broken exported geometry |
| Provenance | Prompt, route, actual controls and honest model disclosure recorded | “Highest model confirmed” without returned evidence; fictitious generation |

For raster-only requests, editability is not applicable and requires a reason. For supplied masters or explicitly direct vector requests, generation can be not applicable with a reason; the source/master and visual review are still required. A requested exact model that cannot be verified remains an unresolved requirement.

## Review record

Copy `assets/review-template.json` into the output project. All template gates start pending. Set `delivery` to `raster`, `full-vector` or `hybrid`. Record generated output and final artefacts under `files` using unique project-relative paths, descriptive roles and actual SHA-256 hashes. Required roles are `brief`, `sources`, `prompt`, `preview`, `caption`, and `visual-comparison`; editable modes also need `source` and `edit-test`. If generation is legitimately not applicable, `prompt` is not required. `visual-comparison` can contain review notes and links to the compared images; it must describe what was actually viewed.

Each gate has `status`, `reviewer`, `notes` and `evidence` (a non-empty list of registered file paths). Allowed final statuses are `pass` and narrowly justified `not_applicable`; `pending` and `fail` keep the release incomplete. Notes identify checks and defects, not just “looks good”. Record unresolved defects in `unresolved`; any entry blocks a final claim.

For `full-vector`, register an SVG `source` and require the SVG audit to pass with live text. Other editable source formats can be described in the record, but this checker currently validates only SVG full-vector releases. Do not relabel an unsupported format to bypass the limitation.

Run:

```sh
python scripts/audit_svg.py output/figure.svg --full-vector --live-text
python scripts/check_release.py output/review.json
```

Both scripts use Python 3.10+ and the standard library. Exit code 0 means their documented checks pass; non-zero means incomplete or failed. Output explicitly states that science and aesthetics are not automatically verified. SHA-256 checks bind the record to file versions, not to the truth of its contents. A fabricated review can still deceive a bookkeeping checker and is forbidden by this skill.

## Practical release review

1. Check science against source evidence and the fixed brief. Never approve solely by familiarity with how the object usually looks.
2. Inspect each final output; compare with the selected master or relevant visual benchmark. Recheck after every change that affects meaning or appearance.
3. Perform the promised editor test in a separate copy, leaving the scientifically correct source intact. Record application and version when available.
4. Correct defects, regenerate hashes and rerun affected checks. Do not endlessly repeat checks unaffected by a change.
5. If a gate cannot pass, return the useful draft and the exact limitation. The task may be partially delivered, but the failed requirement is not complete.

## Maintaining this skill

Run the bundled unit tests and scenario reviews after changing the gates, model policy or reconstruction workflow. Unit tests do not constitute a live image2-to-vector evaluation. For a live evaluation, archive permitted prompts, generated masters, editable exports, matched comparisons and genuine gate records; disclose date, tool route and evaluator. Do not republish private user assets as examples.
