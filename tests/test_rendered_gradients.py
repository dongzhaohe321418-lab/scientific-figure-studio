"""Optional real-render regression; synthetic colours are not measured data.

Requires Pillow, Node.js and Sharp. Set FIGURE_NODE to a Node executable and/or
FIGURE_NODE_MODULES to a directory containing Sharp when not on the usual paths.
"""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from fit_svg_region import fit_region, write_svg
try:
    from PIL import Image
except ImportError:
    Image = None

JS = """
const fs=require('fs'),path=require('path');
let sharp;
try{sharp=require('sharp')}catch(e){
 if(!process.env.FIGURE_NODE_MODULES)throw e;
 sharp=require(path.join(process.env.FIGURE_NODE_MODULES,'sharp'));
}
(async()=>{
 const [input,output,width]=process.argv.slice(1);
 await sharp(fs.readFileSync(input)).resize({width:Number(width)}).png().toFile(output);
})().catch(e=>{console.error(e.message);process.exitCode=1});
"""
NS = {"s": "http://www.w3.org/2000/svg"}


@unittest.skipIf(Image is None, "Rendered gradient checks require Pillow")
class RenderedGradients(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = os.environ.get("FIGURE_NODE") or shutil.which("node")
        if not cls.node:
            raise unittest.SkipTest("Optional rendered checks require Node.js")
        probe = subprocess.run([cls.node, "-e", JS.split("(async()=>")[0]],
                               capture_output=True, text=True, timeout=20)
        if probe.returncode:
            raise unittest.SkipTest("Optional rendered checks require Sharp")

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name)
        self.source = self.base / "synthetic.png"
        image = Image.new("RGB", (64, 81))
        # A flat lower region reveals contamination from the dark first row.
        # Dense sample rows meet on fractional raster coordinates.
        for y in range(81):
            t = min(1, y / 16)
            colour = tuple(round(a + (b-a)*t) for a, b in
                           zip((8, 20, 65), (70, 182, 120)))
            for x in range(64):
                image.putpixel((x, y), colour)
        image.save(self.source)

    def error(self, root, name, scale=1):
        svg = self.base / (name + ".svg")
        png = self.base / (name + ".png")
        write_svg(root, svg)
        subprocess.run([self.node, "-e", JS, str(svg), str(png), str(64*scale)],
                       check=True, capture_output=True, text=True, timeout=30)
        with Image.open(png) as image:
            self.assertEqual(image.size, (64*scale, 81*scale))
            rgba = image.convert("RGBA")
            self.assertEqual(rgba.getchannel("A").getextrema(), (255, 255))
            # Ignore clipped exterior edges and the intentionally changing top.
            return max(abs(rgba.getpixel((32*scale, y))[c] - colour)
                       for y in range(24*scale, 77*scale)
                       for c, colour in enumerate((70, 182, 120)))

    def test_dense_bands_render_without_base_colour_stripes(self):
        for rows in (65, 81):
            for scale in (1, 2):
                with self.subTest(rows=rows, scale=scale):
                    root, _ = fit_region(self.source, columns=3, rows=rows)
                    self.assertLessEqual(self.error(root, f"fixed-{rows}-{scale}", scale), 3)

    def test_subpixel_overlap_mutation_exposes_visible_stripes(self):
        root, _ = fit_region(self.source, columns=3, rows=65)
        step = 100 / 64
        old_height = step + min(.5, step*.1)
        bands = root.findall(".//s:g[@clip-path='url(#colour-region-clip)']/s:rect", NS)
        for band in bands[1:]:
            band.set("height", f"{old_height:.8f}")
        root.find(".//s:linearGradient[@id='colour-region-fade']", NS).set("y2", f"{step/old_height:.10f}")
        self.assertGreater(self.error(root, "old-overlap"), 8)


if __name__ == "__main__":
    unittest.main()
