import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_starttimaarat_oikein(self):
        saldo = self.kassapaate.kassassa_rahaa
        edu = self.kassapaate.edulliset
        mau = self.kassapaate.maukkaat
        self.assertEqual([saldo,edu,mau], [100000,0,0])
    
    def test_kateisostot_toimivat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
        #10
        self.assertEqual(self.kassapaate.edulliset, 1)
        #1
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        #100240
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        #230
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        #100240
        self.assertEqual(self.kassapaate.edulliset, 1)
        #1
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(430),30)
        #30
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        #100640
        self.assertEqual(self.kassapaate.maukkaat, 1)
        #1
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230), 230)
        #230
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        #100640
        self.assertEqual(self.kassapaate.maukkaat, 1)
        #1

    def test_korttiostot_toimivat(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        #edullinen osto onnistuu
        self.assertEqual(str(self.maksukortti),"saldo: 7.6")
        #saldo kortilla oikea onnistuneen oston jälkeen
        self.assertEqual(self.kassapaate.edulliset, 1)
        #myytyjen määrä kasvanut oikein
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        #maukas osto onnistuu
        self.assertEqual(str(self.maksukortti),"saldo: 3.6")
        #kortin saldo oikein
        self.assertEqual(self.kassapaate.maukkaat, 1)
        #myytyjen maukkaiden määrä oikein
        koyhakortti = Maksukortti(220)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(koyhakortti))
        #ei maksutapahtumaa
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(koyhakortti))
        #ei tapahtumaa edullisellakaan
        self.assertEqual(str(koyhakortti), "saldo: 2.2")
        #ei muutosta saldossa
        self.assertEqual(self.kassapaate.maukkaat,1)
        #ei muutosta määrässä
        self.assertEqual(self.kassapaate.edulliset,1)
        #ei muutosta määrässä
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        #ei muutoksia käteiskassassa
    
    def test_kortin_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

        self.assertIsNone(self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-20))


