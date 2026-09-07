"""Synthetic fixtures test tooling, not live image generation or scientific quality."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_svg import audit
from check_release import check, GATES

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
<defs><linearGradient id="shade"><stop stop-color="#9ab"/><stop offset="1" stop-color="#def"/></linearGradient></defs>
<g id="component"><rect width="160" height="60" fill="url(#shade)"/>
<text x="10" y="30">Synthetic fixture</text></g></svg>'''


class QualityTools(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def svg(self, content):
        path = self.base / "figure.svg"
        path.write_text(content, encoding="utf-8")
        return path

    def record(self, generated=True):
        record = json.loads((ROOT / "assets/review-template.json").read_text())
        record["title"] = "Synthetic tooling fixture, not an evaluated figure"
        record["generation"].update(status="complete" if generated else "not_applicable",
            route="codex-native" if generated else None,
            tool="synthetic-test" if generated else None,
            reason="Explicit direct vector test fixture" if not generated else "")
        roles = ["brief", "sources", "preview", "caption", "visual-comparison", "edit-test", "source"]
        if generated:
            roles += ["prompt", "master"]
        for role in roles:
            name = "figure.svg" if role == "source" else role + ".txt"
            path = self.base / name
            path.write_text(SVG if role == "source" else "Synthetic evidence for unit tests only.", encoding="utf-8")
            record["files"].append({"path": name, "role": role,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        for gate in GATES:
            record["gates"][gate].update(status="pass", reviewer="synthetic test fixture",
                notes="Fixture only; no live figure inspection occurred.", evidence=["brief.txt"])
        return record

    def test_valid_vector_with_gradient_and_live_text(self):
        self.assertFalse(audit(self.svg(SVG), True, True)["errors"])

    def test_raster_wrapper_rejected(self):
        wrapped = '<svg xmlns="http://www.w3.org/2000/svg"><image href="data:image/png;base64,AA=="/><text>Label</text></svg>'
        self.assertTrue(audit(self.svg(wrapped), True, True)["errors"])

    def test_outlined_text_does_not_count_as_live_text(self):
        self.assertTrue(audit(self.svg(SVG.replace('<text x="10" y="30">Synthetic fixture</text>', '<path d="M0 0L1 1"/>')), True, True)["errors"])

    def test_external_dependency_rejected(self):
        self.assertTrue(audit(self.svg(SVG.replace('fill="url(#shade)"', 'fill="url(https://example.org/fill.svg)"')), True, True)["errors"])

    def test_duplicate_ids_rejected(self):
        self.assertTrue(audit(self.svg(SVG.replace('<rect width=', '<rect id="component" width=')), True, True)["errors"])

    def test_dtd_rejected(self):
        self.assertTrue(audit(self.svg('<!DOCTYPE svg [<!ENTITY x "x">]>' + SVG))["errors"])

    def test_pending_template_rejected(self):
        template = json.loads((ROOT / "assets/review-template.json").read_text())
        self.assertTrue(check(template, self.base))

    def test_honest_unknown_native_model_is_allowed(self):
        self.assertEqual(check(self.record(), self.base), [])

    def test_unverifiable_highest_model_rejected(self):
        record = self.record()
        record["generation"]["claims_highest_verified"] = True
        self.assertTrue(any("Highest" in e for e in check(record, self.base)))

    def test_exact_model_unknown_rejected(self):
        record = self.record()
        record["generation"]["exact_model_required"] = True
        self.assertTrue(any("Exact model" in e for e in check(record, self.base)))

    def test_reported_model_without_evidence_rejected(self):
        record = self.record()
        record["generation"]["reported_model"] = "gpt-image-2"
        self.assertTrue(check(record, self.base))

    def test_wrong_exact_model_rejected(self):
        record = self.record()
        record["generation"].update(exact_model_required=True, reported_model="gpt-image-1.5",
                                     reported_model_evidence=["brief.txt"])
        self.assertTrue(any("does not match" in e for e in check(record, self.base)))

    def test_model_flags_must_be_boolean(self):
        record = self.record()
        record["generation"]["exact_model_required"] = "false"
        self.assertTrue(any("boolean" in e for e in check(record, self.base)))

    def test_missing_visual_review_rejected(self):
        record = self.record()
        record["gates"]["visual"]["evidence"] = []
        self.assertTrue(any("visual" in e for e in check(record, self.base)))

    def test_changed_source_hash_rejected(self):
        record = self.record()
        self.svg(SVG + "\n")
        self.assertTrue(any("SHA-256" in e for e in check(record, self.base)))

    def test_unresolved_scientific_error_rejected(self):
        record = self.record()
        record["unresolved"] = ["Reversed carrier arrow"]
        self.assertTrue(check(record, self.base))

    def test_direct_vector_exception(self):
        self.assertEqual(check(self.record(generated=False), self.base), [])

    def test_generation_exemption_needs_reason(self):
        record = self.record(generated=False)
        record["generation"]["reason"] = ""
        self.assertTrue(check(record, self.base))

    def test_path_traversal_rejected(self):
        record = self.record()
        record["files"][0]["path"] = "../secret.txt"
        self.assertTrue(any("relative paths" in e for e in check(record, self.base)))

    def test_absolute_windows_path_rejected_on_all_platforms(self):
        record = self.record()
        record["files"][0]["path"] = "C:/private/file.txt"
        self.assertTrue(any("relative paths" in e for e in check(record, self.base)))

    def test_raster_allows_editability_exemption(self):
        record = self.record()
        record["delivery"] = "raster"
        record["gates"]["editability"] = {"status": "not_applicable", "notes": "Raster-only request"}
        self.assertEqual(check(record, self.base), [])

    def test_science_cannot_be_exempted(self):
        record = self.record()
        record["gates"]["science"]["status"] = "not_applicable"
        self.assertTrue(check(record, self.base))

    def test_every_local_markdown_link_resolves(self):
        import re
        for md in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                self.assertTrue((md.parent / target.split("#")[0]).exists(), (md.name, target))


if __name__ == "__main__":
    unittest.main()
