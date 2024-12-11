import unittest

def area(a):
    # The area of the square is squared
    return a * a

def perimeter(a):
    # Multiply the perimeter of square a by 4
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(5), 25)
    

    def test_perimeter(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(5), 20)

