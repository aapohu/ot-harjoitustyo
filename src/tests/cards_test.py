import unittest
from cards import Card, Deck


class Test_cards(unittest.TestCase):
    def setUp(self):
        self.testdeck = Deck()

    def test_correct_amt_of_cards_generated(self):
        self.assertEqual(len(self.testdeck.deck),52)
