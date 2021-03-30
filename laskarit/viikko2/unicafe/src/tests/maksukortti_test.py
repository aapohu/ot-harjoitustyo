import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikea(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
    
    def test_rahan_otto_vahennys_oikein(self):
        self.maksukortti.ota_rahaa(555)
        self.assertEqual(str(self.maksukortti),"saldo: 4.45")

    def test_rahan_otto_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_true_jos_otto_onnistui(self):
        tests = []
        tests.append(self.maksukortti.ota_rahaa(300))
        tests.append(self.maksukortti.ota_rahaa(900))
        self.assertEqual(tests, [True,False])