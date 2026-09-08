# Visual design and review

The target is a clear, refined scientific argument. No single palette, white background or three-dimensional view is compulsory for every field. Establish a suitable visual grammar from inspected references and the user's purpose.

## Quality priority

Scientific accuracy is the prerequisite for both formats. Among correct candidates, protect the best PNG first, then improve SVG fidelity towards it. The easier-to-edit representation must not set a lower ceiling for the PNG. A vector-derived PNG is eligible only when comparison supports its selection; format consistency alone is not a reason.

Review the primary PNG and the SVG render separately. Preserve the raster's composition, contour quality, material character and meaningful detail; document losses in the vector reconstruction. Do not ask image2 for a simpler, flatter image merely to reduce reconstruction effort. More pixels, more SVG paths or a claimed quality score are not substitutes for visual inspection.

## Reference-led design brief

Record observations rather than the vague instruction “make it Nature quality”:

| Attribute | Design decision | Inspection question |
| --- | --- | --- |
| Message | One main claim per panel | Can the reader explain the mechanism without reading every label? |
| Geometry | Coherent orthographic or shallow perspective when useful | Do shared edges and exploded alignments remain consistent? |
| Material | Controlled hue/value, restrained gradients, selective texture | Does appearance distinguish function without inventing microstructure? |
| Hierarchy | Structure first, mechanism second, labels third | Is the focal scientific relationship immediately visible? |
| Colour | Stable semantics across panels and legends | Are charges/functions still identifiable without colour alone? |
| Arrows | Consistent head, shaft, contrast and endpoints | Are transport and light paths unambiguous at print size? |
| Type | One compatible family and a small deliberate size hierarchy | Are labels legible, correctly typeset and free of overlaps? |
| Layout | Aligned panels, short leaders, balanced whitespace | Does spacing support comparison rather than decoration? |

Use colour plus labels, shapes or line styles. Check greyscale and common colour-vision deficiencies where colour carries meaning. Fine pale lines, tiny labels and subtle red/green distinctions often fail at publication size.

## Restraint with depth

Appropriate shallow perspective, edge shading and gentle gradients can reveal layer thickness, interface continuity and material differences. Retain these in SVG using polygons, gradients, masks and clip paths where supported. Uniform flat slabs may be appropriate for a mechanism inset; they are not automatically an adequate replacement for a refined device rendering.

Avoid bloom, lens flare, glowing particles, metallic everything, excessive gloss, heavy drop shadows and generic futuristic styling unless the scientific message explicitly calls for them. Light and charge symbols must carry defined information. Do not make every surface visually compete.

## Three-scale review

1. **Whole figure:** inspect panel balance, hierarchy, palette and obvious scientific errors.
2. **Intended output size:** inspect actual label readability, arrow visibility, line weights and leader ambiguity. Use the target journal's current author instructions if journal compliance is requested; do not invent universal Nature font or DPI requirements.
3. **Enlarged details:** inspect joins, clipping, masks, tangent collisions, arrowheads, formula characters and raster artefacts.

For reconstruction, view the master and exported source side by side at matched dimensions and background. A difference image may reveal omissions; pixel similarity cannot prove science, typography or semantic editability. Explain scientifically justified changes before treating visual differences as defects.

## Reject these substitutions

- “A larger image is automatically a better image.” Native detail, typography and structure matter; upsampling is not new detail.
- “The XML parses, therefore the illustration is finished.” XML says nothing about composition or scientific meaning.
- “SVG cannot reproduce polished shading.” Many refined scientific illustrations use editable gradients and carefully constructed geometry.
- “A weighted 9/10 score cancels one reversed arrow.” Critical errors remain blocking regardless of aesthetic scores.
- “Every figure must resemble one successful tandem cell example.” Transfer design principles, not irrelevant geometry, colours or device structure.
