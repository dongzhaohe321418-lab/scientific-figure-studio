# Actual local editor test

Executed 8 September 2026 in the Codex in-app Chromium browser. The supplied self-contained HTML editor was served on loopback HTTP, port 8770. No remote upload service or model call was involved in editing.

1. Import the canonical `neural-network.svg` through the real file chooser. The page enumerates 188 editable objects.
2. Change `panel-a-title` to `Multilayer perceptron` through the text field and Apply button.
3. Recolour `layer-0-unit-1` to `#ad7846` through the colour control. The editor creates a separate gradient for that object, preserving other nodes. Initial inspection revealed that opacity-based recolouring exposed lines behind the node. The supplied local editor was corrected to use opaque colour tints and the complete save/reopen/export test was repeated. Final gradient stops were `#e8d9cb` and `#ad7846`, with default opacity 1. This intentional test colour is not the canonical layer convention.
4. Select `forward-flow`, enter x=0/y=8 and use Move. Observed transform: `translate(0 8)`.
5. Click Save SVG and verify the actual download on disk. The repeated final test was saved as `neural-network-edited (1).svg` by the browser.
6. Reload the editor, reopen that downloaded file through the real chooser, and inspect the displayed SVG DOM: the edited label, gradient colour, translation and all 188 objects remain.
7. Export PNG from this reopened file, verify its real download and inspect it visually. Archive both files as `edit-test-copy.svg/png`. Canonical deliverables remain unchanged.

This tests the bundled editor on localhost, not Inkscape, Illustrator or direct double-click HTML opening. The basic editor replaces the entire contents of a selected text element; use a full vector editor or the retained generator for sophisticated edits to multi-span mathematics. SVG text remains live text and tspan objects.
