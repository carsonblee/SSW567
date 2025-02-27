"""
HW00b: Triangle Classification
@author Carson Lee
Date: 27 February 2025
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

This code is from the previous assignment hw00b, but is used in this assignment
as the code to be tested.
"""

def classify_triangles(a_side, b_side, c_side) -> str:
    """
    Classifies triangles based on sides.

    Args:
        a_side : length of side a
        b_side : length of side b
        c_side : length of side c

    Returns:
        (str, bool) : Classification of triangle and if it's a right triangle
    """
    #Right Triangle Check
    if((a_side**2 + b_side**2 == c_side**2) or
       (a_side**2 + c_side**2 == b_side**2) or
       (b_side**2 + c_side**2 == a_side**2)):
        right = True
    else:
        right = False

    #Equilateral Check
    if(a_side == b_side and b_side == c_side):
        return ("Equilateral", right)

    #Isosceles Check
    if((a_side == b_side and b_side != c_side) or
         (a_side == c_side and a_side != b_side) or
         (b_side == c_side and a_side != b_side)):
        return ("Isosceles", right)

    #Scalene Check
    if(a_side != b_side and b_side != c_side and c_side != a_side):
        return ("Scalene", right)
