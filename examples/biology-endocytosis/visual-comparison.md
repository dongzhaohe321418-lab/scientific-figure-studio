# Actual visual and scientific review

Reviewer: executing Codex agent, 8 September 2026. This is a self-review, not independent peer review.

## Inspection evidence

The two native-generation outputs were inspected as images. The vector source was rendered to PNG with Sharp/libvips and inspected at full-figure and original-resolution views. The manuscript reference images were inspected separately as described in sources.md. The saved editor test copy was also rendered and visually inspected before the review was marked complete.

## Defects detected and corrected

- Initial image2 output: misspelling of Cytosol, ambiguous left-side leader assignments, absent requested GTP annotation, absence of the last surface membrane and an arrow that could imply coat reassembly rather than removal. The second generation corrected these while preserving the basic appearance.
- First vector reconstruction: coat opening on the wrong side of the connected pit and crowding of the three cargo symbols. The coat's open sector was moved to the neck side; receptor locations/scale were adjusted to keep separate ligand symbols and correct membrane crossing.
- Final reconstruction: remove cargo from the standalone receptor legend and position cargo symbols against receptor heads; keep the visual language consistent without implying molecular stoichiometry.

## Science checks on the selected final SVG/PNG

Four stages remain ordered. The pit is connected to extracellular space; detached vesicles have closed bilayers and visible separation from the plasma membrane. Cargo stays on the extracellular/lumenal side of receptors. AP2 and clathrin remain on the cytosolic side. Dynamin is confined to the connected pit neck. Coat-removal arrow points outward towards released coat glyphs; uncoating leaves a complete membrane. Labels specify GTP-dependent scission and ATP-dependent Hsc70/auxilin uncoating without invented nucleotide stoichiometry.

## Appearance and fidelity

The SVG preserves the master's four-panel information hierarchy, restrained warm/teal/blue/plum palette, rounded bilayer/protein glyphs, subtle material gradients and separate uncoating annotation. The lattice is deliberately reconstructed as a simplified cross-sectional scaffold, with fewer adaptor glyphs to represent selected factors. It is not a pixel-identical tracing or a claim of atomic structural fidelity.

The inspected PNG has legible dark annotations on white, no overlapping cargo symbols, separated process arrows and no clipped footer. The figure is intended for a wide overview (approximately 240 mm) or full-screen use; narrow journal-column legibility is not claimed. Greyscale interpretation is supported by explicit labels and distinct glyph shapes; no formal colour-vision simulation was run.

## Limits

This validates this conceptual example only. It does not establish all biology coverage, quantitative performance or compatibility with untested commercial vector applications. The initial draft is archived only as a documented failure case.
