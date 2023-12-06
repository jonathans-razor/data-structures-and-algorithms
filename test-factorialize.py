import unittest
from factorialize import factorialize  # assuming factorialize function is in factorialize.py

class TestFactorialize(unittest.TestCase):
    def test_factorialize_positive(self):
        self.assertEqual(factorialize(5), 120)
        self.assertEqual(factorialize(3), 6)
        self.assertEqual(factorialize(1), 1)

    def test_factorialize_zero(self):
        self.assertEqual(factorialize(0), 1)

    def test_factorialize_negative(self):
        self.assertIsNone(factorialize(-1))
        self.assertIsNone(factorialize(-10))

if __name__ == '__main__':
    unittest.main()