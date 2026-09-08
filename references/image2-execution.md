# Image2 execution and truthful model selection

## Compatibility

Default support is Codex with a callable built-in image generation tool, image inspection and local file tools. Codex installation alone does not guarantee that this tool is enabled. Other agents require an explicit adapter; this repository does not contain one or supply model access.

GPT Image 2 is not exclusive to Codex. The near-Codex-only limitation concerns this skill's integrated default workflow. API use can involve separate credentials, account eligibility and billing; never switch routes silently.

## Resolve “highest version” at execution time

1. Inspect local tool documentation and the actual callable schema. For version-sensitive claims, check the current [official model page](https://developers.openai.com/api/docs/models/gpt-image-2) and [image generation guide](https://developers.openai.com/api/docs/guides/image-generation).
2. Prefer the most capable officially documented and available **GPT Image 2** option. An alias, a dated snapshot and a quality setting are different things. Never invent `gpt-image-2-pro`, `max` or an undocumented successor. A newer unrelated model family is not an implicit substitute for image2.
3. Native Codex route: use the built-in tool exposed in the current session. If it lacks `model`, `quality` or `size`, do not pass them or claim to have set them. Express visual quality in the prompt; report actual dimensions after generation. Record the backend as undisclosed unless tool metadata identifies it.
4. If exact model pinning is a hard requirement and native routing cannot establish it, explain the limitation. An explicitly authorised API route may set a verified model ID and supported `quality: high`. Use an available maintained image-generation CLI/skill when provided; do not assume a universal executable path. This repository does not implement an API client.
5. Never silently downgrade on missing access or failure. Use an authorised alternative if one exists; otherwise deliver the prepared brief as incomplete with the capability gap stated. Do not repeatedly ask for permission already given in the session.

## Verified documentation snapshot: 8 September 2026

The official model page identifies `gpt-image-2` as a leading image generation/editing model. The API guide exposes `quality: high`, flexible sizes, and transparent PNG/WebP output in preview. Outputs above 3,686,400 pixels are experimental. Recheck these changing capabilities rather than treating the snapshot as permanent. A current tool or CLI can expose fewer controls than the API.

Prefer a supported resolution suited to the actual figure and publication size. Maximum dimensions are not inherently the most reliable choice. Native prompt requests for a size or transparency are intentions; verify the saved output. Do not apply API-only options to native tools.

## Prompt template

```text
Purpose: Original scientific editorial illustration for [audience/output].
Scientific message: [one sentence].
Architecture and conditions: [specific variant; assumptions].
Panel plan: [panel roles and relative layout].
Fixed structure: [ordered components; interfaces; connections].
Mechanism: [species/signal, origin, path, destination and direction].
Exact labels: [verbatim labels, symbols, subscripts/superscripts].
Scale: [to-scale dimensions with sources, or explicit schematic convention].
Visual references: [each input's role and observed transferable attributes].
Visual treatment: [projection, hierarchy, material cues, palette, type, lines].
Quality priority: Optimise the scientifically correct PNG; do not simplify appearance for later SVG reconstruction.
Composition: [clear leaders, whitespace, separation of structure/mechanism].
Constraints: No additional layers, invented data, reversed arrows or unrelated effects.
Editing invariants, if applicable: [what must remain identical].
Target: [requested aspect and intended output size, subject to tool support].
```

Use explicit carrier and optical paths instead of asking the model to infer a mechanism from material abbreviations. For dense diagrams, reserve clean annotation space and construct labels accurately; ensure the final PNG itself contains correct labels, not only the later SVG. Inspect for duplicate or stale generated labels. Corrections/compositing must preserve the best raster appearance and follow the available image-editing tool's instructions. Do not offload design decisions to “journal quality” or flatten the master for vector convenience.

## Native tool handling

Discover the tool rather than hardcoding its namespace. In hosts exposing `referenced_image_paths` and `num_last_images_to_include`, use only one mechanism, following that host's documentation. Inspect local input images first. Do not include references on a brand-new unreferenced generation. If the host uses other arguments, use its actual schema.

Follow the tool's wait and output-display protocol. Save the actual selected output into the project when used as a deliverable; do not leave final links pointing only to an ephemeral location. Save non-destructive numbered versions.

## Provenance record

Record route, actual tool name, requested family/model, model requested in API parameters if any, model reported by the tool if any, supported controls actually sent, prompt path, generation date and output path. Store unknowns as `null`. Request parameters prove what was requested, not necessarily an undisclosed server implementation. Never publish credentials or hidden system prompts.
