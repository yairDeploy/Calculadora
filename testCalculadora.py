# -*- coding:utf -*-
import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def test_suma_2_mas_2(self):
        calc = Calculadora()
        self.assertTrue(4, calc.suma(2, 2))

    def test_suma_5_mas_6(self):
        calc = Calculadora()
        self.assertTrue(11, calc.suma(5, 6))

    def test_suma_menos_5_mas_6(self):
        calc = Calculadora()
        self.assertTrue(5, calc.suma(-5, 10))


if __name__ == '__main__':
    unittest.main()
