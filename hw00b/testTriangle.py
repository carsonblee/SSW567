"""
@author: Carson Lee
"""
import unittest
import triangleClassification

# TEST EQUILATERAL TRIANGLES
class TestEquilateral(unittest.TestCase):

    def testEquilateralNonRight(self): 
        self.assertEqual(triangleClassification.classify_triangles(3,3,3),("Equilateral", False), "Equilateral non-right triangle error")


# TEST ISOSCELES TRIANGLES
class TestIsosceles(unittest.TestCase):

    def testIsoscelesRight(self): 
        self.assertEqual(triangleClassification.classify_triangles(7,7,98**0.5),("Isosceles", True), "Isosceles right triangle error")

    # Where A + B are equal
    def testIsoscelesNonRightAB(self): 
        self.assertEqual(triangleClassification.classify_triangles(3,3,5),("Isosceles", False), "Isosceles (AB sided) non-right triangle error")

    # Where A + C are equal
    def testIsoscelesNonRightAC(self): 
        self.assertEqual(triangleClassification.classify_triangles(5,3,5),("Isosceles", False), "Isosceles (AC sided) non-right triangle error")

    # Where B + C are equal
    def testIsoscelesNonRightBC(self): 
        self.assertEqual(triangleClassification.classify_triangles(4,5,5),("Isosceles", False), "Isosceles (BC sided) non-right triangle error")


# TEST SCALENE TRIANGLES
class TestScalene(unittest.TestCase):

    def testScalenelRight(self): 
        self.assertEqual(triangleClassification.classify_triangles(3,4,5),("Scalene", True), "Scalene right triangle error")

    def testScalenelNonRight(self): 
        self.assertEqual(triangleClassification.classify_triangles(5,6,7),("Scalene", False), "Scalene non-right triangle error")

if __name__ == '__main__':
    unittest.main()