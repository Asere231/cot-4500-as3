import unittest
from ..main.assignment_3 import euler_method, runge_kutta_method, differential_equation
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class TestNumericalMethods(unittest.TestCase):

    def test_euler_method(self):
        result = euler_method(differential_equation, 0, 1, 2, 10)
        self.assertAlmostEqual(result, 1.2446380979332121, places=5)

    def test_runge_kutta_method(self):
        result = runge_kutta_method(differential_equation, 0, 1, 2, 10)
        self.assertAlmostEqual(result, 1.251316587879806, places=5)

if __name__ == '__main__':
    unittest.main()
