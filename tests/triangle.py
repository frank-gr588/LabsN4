import unittest

def area(a, h): 
    #The area of the triangle a multiplied by h divided by two
    return a * h / 2 

def perimeter(a, b, c): 
    #The perimeter of the triangle a plus b plus c
    return a + b + c 


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(5, 10), 25)
        self.assertEqual(area(3, 6), 9)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(7, 8, 9), 24)
