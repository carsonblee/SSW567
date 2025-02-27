# --------------------------------------------------------------------------------
# HW00b: Triangle Classification
# @author Carson Lee
# Date: 27 February 2025
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# 
# This code is from the previous assignment hw00b, but is used in this assignment
# as the code to be tested.
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