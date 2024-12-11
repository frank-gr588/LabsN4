import unittest
import math

def area(r):
    #The area of the circle, pi times r squared
    return math.pi * r * r


def perimeter(r):
    #The perimeter of the circle, pi times r
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimeter(self):
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)