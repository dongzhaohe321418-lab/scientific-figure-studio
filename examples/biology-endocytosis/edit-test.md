# Actual save/reopen/edit test

Executed 8 September 2026 in the Codex in-app Chromium browser using the bundled self-contained SVG editor served from a loopback-only local HTTP server. This exercised real editor controls; no direct source-file mutation was substituted for the UI test.

1. Open `endocytosis.svg` through the browser's file chooser. The editor enumerated 68 semantic objects, including live text, membranes, receptors, adaptors, coats and arrows.
2. Change the live label `coated-vesicle` from `Coated vesicle` to `Clathrin-coated vesicle` with the text controls.
3. Recolour only `released-clathrin-0` to `#4b8c99` with the colour control. This deliberately breaks the scientific legend in a test copy; it is not the final scientific figure.
4. Move `progress-0` with the numeric controls. The saved/reopened transform was `translate(10 12)`.
5. Click Save SVG. A real `endocytosis-edited.svg` file appeared in the user's Downloads directory. The browser automation download event timed out, but filesystem inspection established that the download succeeded.
6. Reload the editor to discard in-memory state, reopen the saved file through the file chooser, and read the displayed DOM: changed label, recoloured component strokes, arrow translation and all 68 editable objects remained.
7. Export PNG from the reopened file. A real `endocytosis-edited.png` was downloaded and inspected. The test copy is archived under `edit-test-copy.svg/png`; the canonical figure is unchanged.

Direct `file://` navigation to the HTML editor was rejected by the automation browser's URL policy. No bypass was attempted. The HTML has no external scripts, fonts or upload endpoints and is designed for local use, but direct double-click opening was not verified in this environment. The actual saved SVG import/edit/download/reopen workflow was verified on localhost. Inkscape, Illustrator and PowerPoint were not tested.
