# Faithful editable reconstruction

## Agree on the scope of editing

| Deliverable | What can be edited | Honest description |
| --- | --- | --- |
| Semantic vector | Components, boundaries, arrows, colours and live text | Fully editable geometry and labels, subject to tested editor support |
| Layered hybrid | Vector annotations and selected geometry; some raster texture/rendering | Partially editable; identify every raster region |
| Raster in SVG/PPTX | Image placement and perhaps overlaid labels | Raster illustration with editable annotations |
| All paths, including outlined letters | Paths and object appearance; text is not normal text | Vector artwork with outlined lettering |

Do not quietly substitute another row for the user's requested editing scope. SVG is a container format, not evidence that all visible content is editable. A PDF may contain raster regions or outlined text. PNG-to-SVG tracing does not recover the original semantic scene.

## Choose a reconstruction method

1. **Semantic vector redraw:** preferred for layered devices, mechanism diagrams and moderate apparatus geometry. Reconstruct meaningful component shapes, not thousands of contour fragments. Text remains live. Use named groups and shared styling.
2. **Hybrid illustration:** appropriate when complex shading or microtexture is required and the requested edits are labels, arrows and selected components. Keep intentional raster layers separate and disclose them. Do not embed the entire picture and call it a conversion.
3. **Editable 3D scene plus vector annotations:** useful for genuinely complex spatial apparatus when modelling is within scope. A rendered PNG is not an editable 3D scene; deliver the actual source scene and relevant assets. Do not introduce Blender when the user explicitly requests image2 without modelling.
4. **Automatic tracing/OCR:** use as an assistant to reconstruction, not as semantic recovery. Repair contours, formulas, ordering, connectors and grouping; compare every critical label. Do not advertise lossless automatic conversion.

For current application-specific import/export instructions, inspect installed versions or official documentation. Do not promise identical support in Inkscape, Illustrator, Affinity, PowerPoint or a browser without testing the relevant application.

## Reconstruction procedure

- Lock an inspected reference master. Inventory components, labels, arrows, legends and panel geometry.
- Use stable IDs such as `layer-active`, `arrow-electron-collection` and `label-detector`. Name groups by scientific meaning rather than drawing order.
- Rebuild geometry with a coherent coordinate system and consistent projection; keep arrows independently selectable.
- Preserve gradients and restrained material cues using vector fills, clipping and opacity. Use filters only where they survive the target editor; inspect exports for unintentional rasterisation.
- Keep live text, correct mathematical typography and a documented font fallback. Optional outlined export copies do not replace the editable master.
- Add an SVG title/description and a concise external caption. Store project-relative references, and package permitted required assets. Avoid remote image/font dependencies for an offline deliverable.
- Provide the actual SVG or native source, not only an editor screenshot. If procedural, include the generator and configuration necessary to reproduce it without hardcoded personal paths.

## Verification

1. Run the structural SVG audit with flags matching the promised mode. Embedded bitmaps, external resource links, duplicate IDs and missing live text are inspectable defects. The audit is not a complete SVG renderer or security validator.
2. Render and inspect the source at matched master size. Check silhouettes, layer ordering, projection, material differences, labels, transport paths and overall balance. Archive side-by-side evidence.
3. Edit a copy in the intended editor: change a scientifically harmless label, recolour a component and move an arrow/component. Save, close/reopen and export. Confirm changes and absence of collateral damage; keep the canonical scientific figure unchanged.
4. If an editor is unavailable, test direct source edits and rendering where possible, but state that application compatibility is unverified. Do not fabricate a successful round trip or pass that release gate.
5. Check offline portability and final export dimensions. Raster resolution is measured from actual pixel dimensions and intended physical size, not a DPI tag alone.
