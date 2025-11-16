import unittest
from calc import add, subtract, multiply, divide, CalcException

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 5), 4)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertAlmostEqual(divide(1, 3), 1/3, places=7)

    def test_divide_by_zero(self):
        with self.assertRaises(CalcException):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
