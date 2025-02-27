# --------------------------------------------------------------------------------
# HW00b: Triangle Classification
# @author Carson Lee
# Date: 28 January 2025
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# 
# DESCRIPTION:
# Write a function classify_triangle() that takes three parameters: a, b, and c. 
# The three parameters represent the lengths of the sides of a triangle. The 
# function returns a string that specifies whether the triangle is scalene, 
# isosceles, or equilateral, and whether it is a right triangle as well.
#
# Triangle Types:
#   - equilateral triangles have all three sides with the same length
#   - isosceles triangles have two sides with the same length
#   - scalene triangles have three sides with different lengths
#   - right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
# --------------------------------------------------------------------------------

def classify_triangles(a, b, c) -> str:
    #Right Triangle Check
    if((a**2 + b**2 == c**2) or
       (a**2 + c**2 == b**2) or
       (b**2 + c**2 == a**2)):
        right = True
    else:
        right = False
    
    #Equilateral Check
    if(a == b and b == c):
        return ("Equilateral", right)
    
    #Isosceles Check
    elif((a == b and b != c) or 
         (a == c and a != b) or
         (b == c and a != b)):
        return ("Isosceles", right)
    
    #Scalene Check
    elif(a != b and b != c and c != a):
        return ("Scalene", right)
    
# # Basic triangle experimentation
# a = 7
# c = (a**2 + a**2)**0.5
# print(a, c)
# print(classify_triangles(a,a,c))