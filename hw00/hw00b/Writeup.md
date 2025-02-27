# HW00b Writeup
Author: Carson Lee, clee27@stevens.edu

Course: SSW 567-A

## What challenges did you encounter with this assignment, if any? 
The one main challenge I faced with this assignment was finding a good way to test for an isosceles right triangle because while they do exist, they don't really exist with all the sides being clean integers. To combat this, I had to do some basic experimentation with the triangle sides to find a suitable testing triangle.

## What did you think about the requirements specification for this assignment?
The requirement specifications for this assignment were clear and concise enough to produce the desired solution. While it might work for something simple like this, larger projects will require more specification for further details.

## What challenges did you encounter with the tools?
The main challenge I encountered with the tools is getting used to using GitHub as well as refamiliarizing myself with the unittest package. While it wasn't that hard to learn, it did take a moment to get back into the swing of things.

## Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?
The criteria for testing was based on if the triangle can exist (for example, an equilateral right triangle cannot) and then a matching up of the different sides (like A == C for isosceles or A == B). Using these criteria, I was able to come up with a total of seven test cases.