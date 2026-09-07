# Scientific Figure Studio

**Research the science. Design with image2. Preserve the quality when making it editable.**

[中文说明](README.zh-CN.md) · [Skill instructions](SKILL.md) · [Quality gates](references/quality-gates.md)

A public, reusable Codex skill for evidence-grounded scientific illustrations: device cross-sections, exploded laboratory apparatus, material mechanisms and explanatory research figures. It addresses a common failure: a refined image becomes a crude diagram when an agent is asked to make it editable.

## Compatibility: primarily Codex

**The default workflow is nearly Codex-only: it depends on Codex's built-in image2 generation capability, image inspection and file tools.** Not every Codex environment exposes these tools. Installing this skill does not unlock a model or provide credentials.

Other agents are not supported out of the box. GPT Image 2 is also available through the OpenAI API, so the model is not exclusive to Codex; adapting this skill elsewhere requires an explicitly configured generation route and equivalent inspection/file capabilities. No standalone API client is included.

## What the skill requires

1. Identify the actual architecture and verify physical relationships using appropriate sources.
2. Inspect scientific figures as well as reading papers; translate observed visual qualities into a concrete design brief.
3. Establish and refine an image2 visual master for substantial new illustrations.
4. When editing is requested, reconstruct meaningful objects while preserving the master's perspective, material cues, typography and hierarchy.
5. Review science, appearance and editability independently; save evidence, prompts, sources and portable deliverables.

Scientific errors cannot be compensated for by attractive styling. File validity cannot substitute for visual inspection. A PNG embedded in SVG is not fully editable. “Nature-style” expresses an aesthetic ambition, not affiliation, acceptance or certification.

## Install

Ask Codex's available skill installer:

```text
Install the skill at the root of this repository:
https://github.com/dongzhaohe321418-lab/scientific-figure-studio
```

For manual installation, place this repository in your Codex skills directory as a folder named `scientific-figure-studio`. For hosts using `CODEX_HOME/skills`, use the configured `CODEX_HOME`; otherwise the common local path is `~/.codex/skills`. Follow your installed host's skill-discovery instructions if it uses a different directory. Do not overwrite an existing installation without reviewing it.

Unix shell example for an unused destination:

```sh
git clone https://github.com/dongzhaohe321418-lab/scientific-figure-studio.git "${CODEX_HOME:-$HOME/.codex}/skills/scientific-figure-studio"
```

PowerShell example for an unused destination:

```powershell
$skillBase = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
git clone https://github.com/dongzhaohe321418-lab/scientific-figure-studio.git (Join-Path $skillBase 'skills/scientific-figure-studio')
```

Start a new Codex conversation if the installed skill is not yet listed. Invoke it explicitly:

```text
$scientific-figure-studio
Create a scientifically accurate two-terminal perovskite/silicon tandem-cell
cross-section. First verify a specific published architecture. Show carrier
transport in a separate mechanism panel. Use restrained editorial styling.
Deliver an image2 visual master and a faithful SVG with live labels and
individually editable components. Preserve material shading and depth.
```

For the best result, supply the intended message, architecture or source paper, an admired visual reference, target size and exactly what must remain editable. For an existing SVG correction, say so; the skill does not force unnecessary image regeneration.

## “Highest image2 version” means a verifiable request

The skill prefers the best verified available GPT Image 2 option and forbids silent downgrades. Native Codex tools may not expose a model selector or quality argument. In that case it reports platform-selected/undisclosed routing instead of falsely claiming a pinned highest snapshot.

An explicitly authorised API route can use a documented model ID and supported `high` quality setting. The skill checks current official documentation rather than inventing a “Pro” version. See [execution details and dated capability snapshot](references/image2-execution.md). Ordinary quality requests do not authorise a silent switch to separately billed API calls.

## Editable deliverables

| Mode | Deliverable |
| --- | --- |
| Full vector | Semantic geometry, separate arrows and live text; SVG source and render |
| Hybrid | Declared raster regions plus editable vector content; layered source and render |
| Raster | Inspected image2 output with prompt, provenance, caption and sources |

Faithful reconstruction can require substantial work. This is an agent workflow, not a one-click lossless PNG-to-SVG converter. Application compatibility must be tested in the actual editor; a browser render alone does not prove Illustrator or PowerPoint compatibility.

## Checks and limitations

Python 3.10+ is required only for the bundled audit scripts; they use the standard library.

```sh
python -m unittest discover -s tests -v
python scripts/audit_svg.py path/to/figure.svg --full-vector --live-text
python scripts/check_release.py path/to/review.json
```

Start a review record from [the template](assets/review-template.json) and follow [the evidence format](references/quality-gates.md). The template intentionally fails until real reviews and files are recorded. Scripts check selected SVG structures, required evidence, file hashes and unsupported completion claims. They do **not** independently establish scientific correctness, visual excellence or the truth of self-reported reviews.

The repository includes synthetic regression tests and [behavioural scenarios](references/regression-cases.md). These are not a live image2-to-editable benchmark. No end-to-end visual success rate or journal acceptance rate is claimed. See [validation status](VALIDATION.md).

## Contribute and reuse

Contributions should include the triggering request, expected behaviour, actual result, and the smallest permitted example. Changes to generation controls need current official documentation; changes to quality checks need regression tests. Do not submit private research, credentials, copyrighted source figures without permission, or unsupported “publication-ready” claims.

The skill, documentation and code are released under the [MIT licence](LICENSE). This licence does not grant rights to third-party reference images or future user inputs. This is an independent project, not an OpenAI or Nature product.
