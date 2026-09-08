"""Mutation tests for the selected scientific invariants in the live examples."""
import unittest, xml.etree.ElementTree as ET
from validate_cases import BASE, CASES, NS, node, path, validate

class CaseChecks(unittest.TestCase):
    def root(self,slug): return ET.parse(BASE/slug/'figure.svg').getroot()
    def fails(self,slug,root): self.assertFalse(validate(slug,root)['passed'])
    def test_all_four_canonical_figures(self):
        for slug in CASES:
            with self.subTest(slug=slug): self.assertTrue(validate(slug,self.root(slug))['passed'])
    def test_missing_hydrogen(self):
        s=CASES[0];r=self.root(s);r.remove(node(r,'p-oh-h'));self.fails(s,r)
    def test_wrong_formal_charge(self):
        s=CASES[0];r=self.root(s);e=node(r,'p-minus');e.clear();e.set('id','p-minus');e.text='+';self.fails(s,r)
    def test_reversed_electron_arrow(self):
        s=CASES[0];r=self.root(s);node(r,'electron-attack').find('s:polygon',NS).set('points','520,929 540,949 535,943');self.fails(s,r)
    def test_two_headed_electron_arrow(self):
        s=CASES[0];r=self.root(s);ET.SubElement(node(r,'electron-attack'),'{'+NS['s']+'}polygon',{'points':'274,923 285,918 280,932'});self.fails(s,r)
    def test_misaligned_static_head(self):
        s=CASES[1];r=self.root(s);node(r,'standpipe').findall('s:rect',NS)[1].set('y','410');self.fails(s,r)
    def test_screen_in_aquitard(self):
        s=CASES[1];r=self.root(s);p=next(p for p in node(r,'standpipe').findall('s:path',NS) if p.get('stroke')=='#455f72');p.set('d','M1451,580 H1485');self.fails(s,r)
    def test_wrong_carbon_destination(self):
        s=CASES[2];r=self.root(s);node(r,'photosynthesis').set('data-destination','microbes');self.fails(s,r)
    def test_solar_energy_counted_as_carbon(self):
        s=CASES[2];r=self.root(s);node(r,'light-energy').set('data-species','carbon');self.fails(s,r)
    def test_wrong_collider_edge(self):
        s=CASES[3];r=self.root(s);e=node(r,'collider-X-C');e.set('data-source','C');e.set('data-destination','X');self.fails(s,r)
    def test_wrong_drawn_causal_arrow(self):
        s=CASES[3];r=self.root(s);node(r,'collider-Y-C').find('s:polygon',NS).set('points','1800,450 1810,435 1790,435');self.fails(s,r)

if __name__=='__main__': unittest.main()
