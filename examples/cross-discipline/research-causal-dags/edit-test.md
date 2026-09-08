# Actual local editor round trip

Date: 8 September 2026. Editor: bundled HTML SVG editor in the Codex Chromium browser, served from loopback HTTP. This record documents actual UI actions, not source-only editing.

1. Imported a local copy of the canonical SVG; 57 semantic objects were available.
2. Changed live `figure-title` to `Three causal diagram motifs` using the text control.
3. Recoloured `confounder-node-Z` to `#c39542` using the colour control.
4. Moved `confounder-X-Y` by x=0, y=8 SVG units using the move controls.
5. Clicked Save SVG and verified a downloaded SVG on disk.
6. Reloaded the editor, reimported that downloaded file, and checked retained title, gradient fill and `translate(0 8)`.
7. Exported a PNG from the reopened SVG, saved it and inspected the actual image.

The archived results are `edit-test-copy.svg` and `edit-test-copy.png`. Opaque gradient recolouring retained shading without exposing underlying strokes. The canonical `figure.svg`/`figure.png` pair is unchanged by these test edits.

Direct file-URL HTML opening was not retested after the earlier browser-policy rejection. Desktop vector applications were not tested. Subsequent basic editing requires no image-generation call or cloud upload. Recheck scientific meaning after any content edit.
