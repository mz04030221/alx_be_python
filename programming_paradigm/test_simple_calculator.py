import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(1, 1), 1)

    def test_division(self):
        self.assertEqual(self.calc.divide(1, 1), 1)
