# Compact computer-science frameworks and matched PNG/SVG delivery

Use this guide for method overviews, model architectures, training pipelines, data flows and agent workflows. It supplements the scientific and visual reviews; it does not replace the discipline-specific checks. Hardware layouts, maps and physical assemblies may need meaningful clearances that a compact algorithm diagram does not.

## Structure before layout

Start from the supplied method, paper or implementation. Keep two short records in the figure project:

- **Semantic relations:** real operations, inputs/outputs, state ownership, branches, training versus inference, tensor dimensions and evidence. Identify assumptions separately.
- **Visible representation:** which operations need a module, which values belong on edges or ports, which details fit inside a grouped operation, and which explanations belong in the caption. Internal IDs do not become display text.

A scalar, weight, threshold or intermediate tensor is not automatically another processing box. Conversely, do not hide a required operation behind an output icon or a generic module title. A comparison or loss operation may legitimately show its two inputs. Keep the main mechanism visible rather than filling its area with prose.

For each nontrivial connector, record the producer, actual consumer, meaning and destination. If A produces x and C consumes it, a neighbouring B must not become an apparent relay merely because it lies between them. Distinguish data flow, parameter updates, fixed-state reuse, metadata and visual callouts. Shared state, gradient flow and optimiser updates are different relations.

## Information density is functional content per readable area

For a method overview, aim for a compact manuscript figure with the main mechanism occupying most of the useful canvas. Do not translate “clean” into large empty bands or a set of tiny isolated boxes.

When a user requests more density:

1. Check for omitted mechanisms first. Restore necessary operations and relationships rather than adding decorative facts.
2. Reduce outer margins, oversized headings and inter-row gaps before reducing type size.
3. Align related operations; group short substeps while retaining their order and internal meaning.
4. Move parameter definitions to their actual edges, ports or local labels. Keep long qualifications in the caption while retaining conditions that change the figure's claim.
5. Show a repeated common pipeline once when possible. Use compact branch differences or labelled reuse; distinguish visual replicas from different scientific instances.
6. Treat context, notes and legends as supporting material unless they are themselves the contribution.

Area budgets are planning aids, not scores or fixed percentage requirements. Record the actual layout change, preserved content and type sizes. Inspect at the intended final width: shrinking text to claim higher density is not a successful repair. Physical geometry takes precedence over compactness where spatial relationships carry the science.

## Compact routing and meaningful depth

Use consistent line families and label their meaning. Keep arrowheads at the intended ports, away from text and non-consuming modules. Separate overview/detail references from process arrows. A detail inset must add source-supported information rather than repeat the full parent workflow.

Replace avoidable page-wide auxiliary rails with short local routes or explicitly paired continuation ports. Both ports must have matching visible identifiers and a documented source/target; a broken or unlabelled arrow is not a continuation. Do not remove a scientific dependency merely to tidy the drawing. Preserve long routes when they genuinely represent a bus, loop, timeline or physical connection.

For moderate 3D, use a consistent shallow projection, distinct top/side/front faces, controlled gradients and fine shared edges. Increase useful facet depth or tonal separation, not glow or indiscriminate surface texture. Keep labels and arrows above surfaces. A network glyph's geometry is schematic unless actual dimensions are supplied.

## When the user requires near-identical PNG and SVG

Follow the [editorial common-master procedure](editorial-refinement.md#4-select-the-final-png-on-quality-then-verify-the-pair). It applies to a suitable existing/direct-vector source and to an image2-assisted SVG refinement that demonstrably meets or improves the best eligible native candidate. Export only after that quality decision, record the rendering conditions, then reopen the saved SVG and independently render its comparison PNG. Inspect both and compare decoded pixels; a source hash or identical filenames alone does not verify parity.

Preserve live text, internal assets and meaningful groups. Test label, colour and position edits in a separate copy, followed by actual saving, reopening and export. Report any unsupported target editor or font fallback. Equality in one rendering environment does not establish identical appearance in every application.

For an image2 master that remains visually superior, keep that master. Improve the vectors until they reach the required appearance; do not replace a better PNG with a crude vector export just to achieve numerical equality. If the requested parity remains unmet, report the gap rather than claim success. “Same source” establishes provenance, not aesthetic quality.

## Review questions

- Is the main operation chain complete, readable and visually dominant?
- Are tensor shapes, branch multiplicity, state ownership and update targets consistent with evidence?
- Have variables become unnecessary modules, or have essential operations disappeared?
- Do any arrows falsely relay data, cross labels, lose an endpoint or confuse callouts with flow?
- Has compaction preserved useful type size and the full mechanism?
- Is depth coherent and editable? Have actual PNG/SVG renders, not just XML, been compared?

## Selective provenance

These rules incorporate selected concepts from [c-narcissus/paper-framework-figure-studio-pro](https://github.com/c-narcissus/paper-framework-figure-studio-pro), package **v3.2.15f**, inspected on 2026-09-09: its semantic/render-graph separation, edge-label treatment, layout-density guidance, false-relay checks and routing/callout guidance. The package declares MIT-0 licensing. This is a concise adaptation, not a vendored dependency or a claim of equivalence.

Its fixed candidate counts, compulsory stage-by-stage waits and reply text, checkpoint machinery and terminal raster-only workflow are not adopted. They do not fit this skill's completed local PNG/SVG delivery. Capability statements in that repository are not authoritative for the current Codex environment; inspect actual tool schemas. The requested scientific object and user-approved scope remain controlling.
