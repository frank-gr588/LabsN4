import unittest

def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(3, 7), 21)

    def test_perimeter(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(3, 7), 20)
