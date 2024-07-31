import unittest
from src.core.morie import MorIE

class TestMorIE(unittest.TestCase):
    def setUp(self):
        self.morie = MorIE()

    def test_positive_scenario(self):
        # Set up the inputs
        self.morie.intent = 1
        self.morie.n1 = 5
        self.morie.n2 = 1
        self.morie.b1 = 0
        self.morie.b2 = 1
        self.morie.dg_i = 1
        self.morie.ig_i = 0.5
        self.morie.db_i = -1
        self.morie.ib_i = -0.5

        # Calculate the moral value
        moral_value = self.morie.calculate()

        # Check if the moral value is correct
        self.assertAlmostEqual(moral_value, 7.0, places=2)

        # Check if the result text is correct
        result_text = self.morie.get_result_text(moral_value, 2.20)  # Using threshold from the image
        self.assertEqual(result_text, "NET POSITIVE")

if __name__ == '__main__':
    unittest.main()