# Editorial refinement without sacrificing the PNG

Use after a suitable image2 master exists, especially when the user requests human-like finishing, greater useful density, refined shallow 3D or closely matched PNG/SVG. This is an editorial pass over the actual artwork, not a new model name or a promise of journal acceptance. Keep the requested scientific meaning and generation provenance.

## 1. Diagnose before changing the style

Save the best scientifically eligible native PNG with a version and hash. Inventory essential structures, operations, labels, equations and connector endpoints. Compare the actual render against the user's benchmark at the intended final size. Write a short discrepancy list, ordered by scientific consequence and visual impact.

| Observed defect | Targeted repair | What must survive |
| --- | --- | --- |
| Sparse method diagram | Restore omitted operations; compact outer margins, headings and gaps | Complete mechanism, readable labels and meaningful clearances |
| Heavy or unnaturally narrow lettering | Retypeset with a suitable normal-width font and limited hierarchy | Exact notation, subscripts, signs and editable text |
| Generic presentation-card appearance | Remove redundant frames, badges or tinted bands; retain meaningful boundaries | Compartment, state or process grouping |
| Flat vector blocks replacing refined structure | Rebuild coherent front/top/side faces, contours and restrained shading | Physical interfaces, occlusion and independent components |
| Smooth fields become striped or posterised | Compare regional gradient sampling, clipping and rendered seams | Source provenance; no claim of recovered measurements |
| Correct labels but ambiguous flow | Reattach the visible shaft and arrowhead to the actual producer/consumer | Branching, direction and scientific meaning |

Do not apply every repair indiscriminately. A biological compartment boundary, circuit enclosure or map frame may carry essential meaning. Neither blank space nor surface detail has a universal optimum. For computing-related figures, also use [compact frameworks](computing-frameworks.md).

## 2. Retypeset and compact deliberately

- Keep real text. Use an available, documented normal-width family suited to the venue, language and notation. Arial/Helvetica are examples, not compulsory fonts for all disciplines. Confirm the actual fallback for Greek, mathematical symbols and non-Latin labels.
- Do not fix collisions by horizontally squeezing glyphs, using `textLength`/`lengthAdjust` to compress labels, or applying unequal text scaling. Reflow wording, move a local label or resize its region first. A justified special use of these SVG features is not automatically an error, but must be checked visually.
- Use a small deliberate hierarchy: panel identifiers, concise titles, body labels and supporting notes. Avoid making every label bold. Keep important conditions visible; only move explanatory detail to the caption when the claim remains intelligible.
- Calculate type at the intended physical width. For a uniformly scaled SVG, approximate points as `font-size × width-mm / viewBox-width × 72 / 25.4`; include any nested transforms. Check actual text at that size. Export DPI metadata does not make tiny lettering readable.
- Inspect formulas character by character against the scientific brief: minus versus dash, multiplication, indices, vector marks, bars, hats and tildes. Live `tspan` elements or separately editable accents can support layout; recheck their alignment and grouping after editing.
- Use rendered text bounds to flag overlaps and out-of-canvas labels. Distinguish genuine collisions from intentional mathematical composition, superscripts and containment. A zero-overlap report is only a diagnostic: also inspect text against paths, arrowheads, boundaries and other objects.

The [Nature research figure guide](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/), consulted on 9 September 2026, supports space-efficient panels, standard editable typography and removal of unnecessary decoration. It is a design reference, not an endorsement. Check the specific journal's current instructions when submission compliance is requested; the PNG/SVG working pair is not automatically its required submission package.

## 3. Preserve useful volume and colour detail

Construct coherent shallow geometry with separately editable faces, shared edges and modest tonal separation. Use broad gradients before adding fine highlights. Avoid glow, repeated glossy textures and unsupported microstructure. Keep labels and mechanism arrows clearly above surfaces.

Recolour components without collapsing all faces to an identical gradient ramp. Clone shared paint definitions for independent edits, keep offsets and opacity, and preserve relative tone where supported. Check that masks, clipping geometry and other instances remain unchanged. The bundled editor's hex-colour retint is an approximate sRGB tone operation, not physical relighting or perceptual colour matching; advanced paint styles need a fuller editor.

For continuous illustrative fields, apply the [regional method](png-to-svg.md). Increase sampling only where matched crops justify the detail gain and file-size cost. Inspect dense bands at the actual export scale; subpixel antialiasing can reveal the base underneath. More stops are not automatically higher fidelity, and a colour-field group does not recover individually editable scientific features. Measured maps and plots must still come from data.

## 4. Select the final PNG on quality, then verify the pair

The native PNG remains the protected benchmark during reconstruction. A carefully refined SVG can become a better final artwork through corrected typography, coherent geometry and scientifically necessary repairs. This is an eligible continuation of the image2 workflow, not an automatic exception to PNG priority.

1. Render the refined SVG separately and inspect it against the best scientifically eligible native candidate at matched canvas, crop and background. Check structure, composition, depth, colour detail, typography and mechanism. Preserve both versions and record concrete gains and remaining losses.
2. Select the SVG-derived primary PNG **only when the visual/scientific comparison supports meeting or improving that benchmark**. Never select it merely because pixel equality is convenient. If the native remains superior, retain it and continue SVG refinement; report any unmet parity request.
3. For an eligible common master, record its hash, renderer/version, actual font environment, viewBox, background and pixel dimensions. Export `figure.png`; reopen the saved `figure.svg` and independently render `figure-svg-preview.png` under the same conditions. Compare decoded images and visually inspect both. Reusing the same PNG bytes is not a second rendering check.
4. Keep schema 2: record generation as actually performed, list native masters, set the selected PNG origin to `svg-render`, and cite the comparison in the existing PNG/SVG quality evidence. An image2-assisted refinement must not be relabelled `not_applicable` generation simply because the final export came from SVG.
5. Report the scope precisely: matching at inspected scales/in the tested renderer, or an approximation with listed differences. Font rendering, masks and gradients may differ in another editor. Similarity metrics and common provenance cannot prove beauty, scientific correctness or semantic editability.

No change is needed to an already excellent native PNG just to satisfy the refinement label. Do not claim that AI output was authored by a human, add fake hand jitter or paper grain, or promise undetectable provenance.

## 5. Finish with a real edit and export check

Recheck the scientific inventory against visible paths and labels after all style edits. Use targeted negative mutations when exact topology, direction or geometry warrants them; generic metadata alone cannot prove endpoint correctness.

In a separate copy, edit a live label, recolour a multi-face component and move an object or arrow. Save to disk, verify file existence, reopen that file, export and inspect. Check that shared resources did not alter unrelated objects and that the canonical artwork stayed intact. Name the actual editor and test scope. Scripted source edits, browser handler tests, user-interface round trips and testing in a desktop vector editor are distinct evidence.

Deliver saved PNG/SVG, the independent SVG preview, retained native versions, editable generators where used, and concise comparison/editing notes. Summarise observed quality, not invented numerical aesthetic scores. User acceptance is useful feedback but does not replace scientific review.
