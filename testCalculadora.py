# -*- coding:utf -*-
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
	
	def test_suma_2_mas_2(self):
		calc = Calculadora()
		self.assertEquals(4,calc.suma(2,2))

	def test_suma_5_mas_6(self):
		calc = Calculadora()
		self.assertEquals(11,calc.suma(5,6))

if __name__ == '__main__':
	unittest.main()		