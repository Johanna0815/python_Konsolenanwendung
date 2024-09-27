import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calc.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_percentage(self):
        result = self.calc.percentage(50, 10)
        self.assertEqual(result, 5)

    def test_percentage_zero(self):
        result = self.calc.percentage(50, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
