"""Deterministic coverage for the optional colour-region helper, not aesthetics."""
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
from fit_svg_region import fit_region, sample_rgb, write_svg
from audit_svg import audit
try:
    from PIL import Image
except ImportError:
    Image = None
NS = {"s": "http://www.w3.org/2000/svg"}


@unittest.skipIf(Image is None, "Optional gradient helper requires Pillow")
class RegionGradients(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.png = self.base/"source.png"
        self.image = Image.new("RGB", (2, 2))
        self.image.putdata([(255,0,0), (0,255,0), (0,0,255), (255,255,255)])
        self.image.save(self.png)

    def test_samples_preserve_corners_and_interpolate(self):
        self.assertEqual(sample_rgb(self.image, 0, 0), (255,0,0))
        self.assertEqual(sample_rgb(self.image, 1, 1), (255,255,255))
        self.assertEqual(sample_rgb(self.image, .5, .5), (128,128,128))

    def test_output_is_vector_with_correct_colour_endpoints(self):
        root, meta = fit_region(self.png, columns=2, rows=2)
        stops=root.findall(".//s:linearGradient[@id='colour-region-row-0']/s:stop",NS)
        self.assertEqual([s.get("stop-color") for s in stops], ["#ff0000","#00ff00"])
        svg=self.base/"region.svg";write_svg(root,svg)
        self.assertEqual(audit(svg, True, False)["errors"], [])
        self.assertEqual(root.findall(".//s:image",NS), [])
        self.assertEqual(root.findall(".//s:text",NS), [])
        self.assertIn("no recovered labels", meta["scope"])

    def test_cropped_rectangle_has_its_own_aspect_and_colours(self):
        root, meta=fit_region(self.png, (1,0,1,2), 2,2)
        self.assertEqual(root.get("viewBox"), "0 0 1 2")
        self.assertEqual(meta["crop_xywh"], [1,0,1,2])
        self.assertEqual(root.find(".//s:linearGradient[@id='colour-region-row-0']/s:stop",NS).get("stop-color"),"#00ff00")

    def test_input_is_unchanged_and_provenance_has_no_local_path(self):
        before=self.png.read_bytes()
        root,meta=fit_region(self.png)
        self.assertEqual(self.png.read_bytes(),before)
        self.assertEqual(meta["source_sha256"],hashlib.sha256(before).hexdigest())
        self.assertNotIn(str(self.base),ET.tostring(root,encoding="unicode"))

    def test_overlapping_bands_are_clipped_and_have_opaque_base(self):
        root,_=fit_region(self.png,columns=3,rows=3)
        paint=root.find(".//s:g[@clip-path='url(#colour-region-clip)']",NS)
        rectangles=paint.findall("s:rect",NS)
        self.assertEqual(rectangles[0].get("height"),"100")
        self.assertGreater(float(rectangles[1].get("height")),50)
        self.assertEqual(root.find(".//s:clipPath/s:rect",NS).get("height"),"100")

    def test_outside_empty_and_fractional_crops_are_rejected(self):
        for crop in [(-1,0,1,1),(0,0,3,1),(0,0,0,1),(0.,0,1,1)]:
            with self.subTest(crop=crop),self.assertRaises(ValueError): fit_region(self.png,crop)

    def test_blend_reaches_next_sample_before_overlap(self):
        root,_=fit_region(self.png,columns=3,rows=3)
        fade=root.find(".//s:linearGradient[@id='colour-region-fade']",NS)
        bands=root.findall(".//s:g[@clip-path='url(#colour-region-clip)']/s:rect",NS)
        # A new band begins at the next sampled row: the previous contribution
        # must already be zero there, otherwise an artificial colour jump appears.
        end=float(bands[2].get("height"))*float(fade.get("y2"))
        next_row=float(bands[3].get("y"))
        self.assertAlmostEqual(end,next_row,places=7)

    def test_transparent_region_is_not_silently_flattened(self):
        Image.new("RGBA",(2,2),(30,60,90,128)).save(self.png)
        with self.assertRaisesRegex(ValueError,"Transparent"): fit_region(self.png)

    def test_invalid_grid_and_ids_are_rejected(self):
        for args in [{"columns":1},{"rows":257},{"rows":True},{"prefix":"bad id"},{"prefix":"xmlns:x"}]:
            with self.subTest(args=args),self.assertRaises(ValueError):fit_region(self.png,**args)

    def test_only_actual_png_is_accepted(self):
        self.image.save(self.png,format="JPEG")
        with self.assertRaisesRegex(ValueError,"actual PNG"):fit_region(self.png)

    def test_srgb_profile_is_converted_without_changing_source(self):
        from PIL import ImageCms
        profile=ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
        self.image.save(self.png,icc_profile=profile)
        before=self.png.read_bytes()
        root,meta=fit_region(self.png,columns=2,rows=2)
        self.assertIn("converted to sRGB",meta["colour_space"])
        self.assertEqual(root.find(".//s:linearGradient[@id='colour-region-row-0']/s:stop",NS).get("stop-color"),"#ff0000")
        self.assertEqual(self.png.read_bytes(),before)

    def test_invalid_profile_is_not_silently_ignored(self):
        self.image.save(self.png,icc_profile=b"not an ICC profile")
        with self.assertRaisesRegex(ValueError,"ICC profile"):fit_region(self.png)

    def test_non_srgb_gamma_requires_explicit_conversion(self):
        import struct
        from PIL.PngImagePlugin import PngInfo
        chunks=PngInfo();chunks.add(b"gAMA",struct.pack(">I",100000))
        self.image.save(self.png,pnginfo=chunks)
        with self.assertRaisesRegex(ValueError,"gamma"):fit_region(self.png)

    def test_existing_output_and_wrong_suffix_are_preserved(self):
        root,_=fit_region(self.png)
        output=self.base/"existing.svg";output.write_text("keep")
        with self.assertRaises(FileExistsError):write_svg(root,output)
        self.assertEqual(output.read_text(),"keep")
        with self.assertRaises(ValueError):write_svg(root,self.png)


if __name__=="__main__":
    unittest.main()
