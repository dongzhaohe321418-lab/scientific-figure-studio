# Faithful editable reconstruction

## Agree on the scope of editing

Default to the best scientifically correct PNG plus a fully editable SVG, saved in a persistent project directory. The primary PNG is selected on its own scientific and visual merits, not forced through SVG. Save the SVG render separately as `figure-svg-preview.png`. The SVG must preserve scientific meaning while its visual fidelity is improved; never reduce the PNG's quality to force a match. Link the files and supply reopening instructions. Change the promised editing scope only for an explicit user request.

| Deliverable | What can be edited | Honest description |
| --- | --- | --- |
| Semantic vector | Components, boundaries, arrows, colours and live text | Fully editable geometry and labels, subject to tested editor support |
| Layered hybrid | Vector annotations and selected geometry; some raster texture/rendering | Partially editable; identify every raster region |
| Raster in SVG/PPTX | Image placement and perhaps overlaid labels | Raster illustration with editable annotations |
| All paths, including outlined letters | Paths and object appearance; text is not normal text | Vector artwork with outlined lettering |

Do not quietly substitute another row for the user's requested editing scope. SVG is a container format, not evidence that all visible content is editable. A PDF may contain raster regions or outlined text. PNG-to-SVG tracing does not recover the original semantic scene.

## Choose a reconstruction method

When reconstructing a selected PNG, first partition scientific structure, text, arrows and colour/texture regions. Follow [PNG-to-SVG methods](png-to-svg.md) for the tested decision process and optional gradient helper. Successful texture reconstruction must not replace semantic geometry or convert live labels into paths.

1. **Semantic vector redraw:** preferred for layered devices, mechanism diagrams and moderate apparatus geometry. Reconstruct meaningful component shapes, not thousands of contour fragments. Text remains live. Use named groups and shared styling.
2. **Hybrid illustration:** appropriate when complex shading or microtexture is required and the requested edits are labels, arrows and selected components. Keep intentional raster layers separate and disclose them. Do not embed the entire picture and call it a conversion.
3. **Editable 3D scene plus vector annotations:** useful for genuinely complex spatial apparatus when modelling is within scope. A rendered PNG is not an editable 3D scene; deliver the actual source scene and relevant assets. Do not introduce Blender when the user explicitly requests image2 without modelling.
4. **Automatic tracing/OCR:** use as an assistant to reconstruction, not as semantic recovery. Repair contours, formulas, ordering, connectors and grouping; compare every critical label. Do not advertise lossless automatic conversion.

For current application-specific import/export instructions, inspect installed versions or official documentation. Do not promise identical support in Inkscape, Illustrator, Affinity, PowerPoint or a browser without testing the relevant application.

## Reconstruction procedure

- Lock the best scientifically correct PNG as the protected visual target. Inventory components, labels, arrows, legends and panel geometry. Preserve versioned raster candidates; SVG work must not overwrite them.
- Use stable IDs such as `layer-active`, `arrow-electron-collection` and `label-detector`. Name groups by scientific meaning rather than drawing order.
- Rebuild geometry with a coherent coordinate system and consistent projection; keep arrows independently selectable.
- Preserve gradients and restrained material cues using vector fills, clipping and opacity. Use filters only where they survive the target editor; inspect exports for unintentional rasterisation.
- Keep live text, correct mathematical typography and a documented font fallback. Optional outlined export copies do not replace the editable master.
- Add an SVG title/description and a concise external caption. Store project-relative references, and package permitted required assets. Avoid remote image/font dependencies for an offline deliverable.
- Provide the actual SVG or native source, not only an editor screenshot. If procedural, include the generator and configuration necessary to reproduce it without hardcoded personal paths.

## Improve SVG quality without penalising PNG

1. Compare the separate SVG render with the primary PNG at matched size. List concrete discrepancies: silhouettes, proportions, surface treatment, spatial depth, annotations and microdetail. Fix the most visually consequential discrepancy first.
2. Replace stock primitives where their shapes are wrong: use fitted Bézier curves, coherent shared boundaries, shaped silhouettes and consistent projection. Preserve named scientific components instead of fragmenting everything into a trace.
3. Reconstruct material appearance with layered gradients, restrained highlights, clipping, masks and selected vector texture. Use reusable symbols/patterns where supported. Textures must not imply measured structure. Check whether the target editor preserves each technique before relying on it.
4. Refine edges, occlusion, line weights, arrowheads and live-text spacing. Group movement must keep arrow shafts/heads and component shading together. Recolouring should retain intentional opacity and shading, as tested by the bundled editor.
5. Inspect the revised render and recheck scientific invariants. Preserve the best SVG revision; reject regressions. If a technique cannot reproduce the target, diagnose that limitation and try another supported representation rather than merely increasing the number of paths.
6. State the actual outcome: visually matched at the inspected scale, or an editable approximation with listed differences. A simpler organic texture may remain visibly inferior. Do not call it lossless or equally polished merely because all elements are vectors. Supply a hybrid alternative only within authorised editing scope; it cannot silently replace a requested full vector.

A ready high-quality PNG may be delivered while SVG refinement continues. Show separate completion statuses. Scientific corrections apply to both files: after changing a mechanism or label in SVG, update and re-review the PNG as necessary without substituting an inferior rendering by default.

## Verification

1. Run the structural SVG audit with flags matching the promised mode. Embedded bitmaps, external resource links, duplicate IDs and missing live text are inspectable defects. The audit is not a complete SVG renderer or security validator.
2. Render and inspect the source at matched master size. Check silhouettes, layer ordering, projection, material differences, labels, transport paths and overall balance. Archive side-by-side evidence.
3. Edit a copy in the intended editor: change a scientifically harmless label, recolour a component and move an arrow/component. Save, close/reopen and export. Confirm changes and absence of collateral damage; keep the canonical scientific figure unchanged.
4. If an editor is unavailable, test direct source edits and rendering where possible, but state that application compatibility is unverified. Do not fabricate a successful round trip or pass that release gate.
5. Check offline portability and final export dimensions. Raster resolution is measured from actual pixel dimensions and intended physical size, not a DPI tag alone.

## Optional local editor

The bundled [SVG editor](../assets/svg-editor.html) is a self-contained HTML file for opening, changing and downloading supported SVGs. It supports live text, per-object colour changes, translation, undo, SVG save and PNG export. It performs no network uploads and is designed to open in a normal desktop browser from disk. It is a deliberately limited SVG subset editor, not a full replacement for Inkscape or Illustrator; unsupported elements/styles are rejected. Editing compound mathematical labels replaces their text content; use a full vector editor for advanced typography or path changes.

The biology example was actually imported, edited, downloaded, reimported and exported through this editor served on localhost in the Codex browser. A direct `file://` navigation was blocked by the automation browser's URL policy, so direct double-click offline opening was not verified in that environment. Do not claim tests that were not performed or bypass browser restrictions.
