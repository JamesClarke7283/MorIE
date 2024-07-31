import unittest
from src.core.morie import MorIE

class TestMorIE(unittest.TestCase):
    def test_positive_scenario(self):
        morie = MorIE()
        morie.intent = 1
        morie.n1 = 5
        morie.b1 = 0
        morie.n2 = 4
        morie.b2 = 1
        morie.dg_i = 1
        morie.ig_i = 0.5
        morie.db_i = -1
        morie.ib_i = -0.5

        moral_value = morie.calculate()
        self.assertAlmostEqual(moral_value, 7.0, places=2)
        self.assertEqual(morie.get_result_text(moral_value, threshold=2.2), "NET POSITIVE")

    def test_negative_scenario(self):
        morie = MorIE()
        morie.intent = -1
        morie.n1 = 3
        morie.b1 = 2
        morie.n2 = 2
        morie.b2 = 2
        morie.dg_i = 1
        morie.ig_i = 0.5
        morie.db_i = -1
        morie.ib_i = -0.5

        moral_value = morie.calculate()
        self.assertAlmostEqual(moral_value, -3, places=2)
        self.assertEqual(morie.get_result_text(moral_value, threshold=0.2), "NET NEGATIVE")

    def test_neutral_scenario(self):
        morie = MorIE()
        morie.intent = 0
        morie.n1 = 0
        morie.b1 = 0
        morie.n2 = 4
        morie.b2 = 2
        morie.dg_i = 1
        morie.ig_i = 0.5
        morie.db_i = -1
        morie.ib_i = -0.5

        moral_value = morie.calculate()
        self.assertAlmostEqual(moral_value, 0.0, places=2)
        self.assertEqual(morie.get_result_text(moral_value, threshold=1), "NEUTRAL")
