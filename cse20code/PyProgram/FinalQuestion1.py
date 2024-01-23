#FinalQuestion1

import math

s = ['circle', 'square', 'equilateral Triangle']

def circle(x):
    x = float(input("enter value for x:"))
    circleArea = math.pi * x * x 
    return circleArea

def square(x): 
    x = float(input("enter value for x:"))
    squareArea = x * x
    return squareArea 

def equilateralTriangle(x): 
    x = float(input("enter value for x:"))
    eqTriArea = (math.sqrt(3)/4)*(x * x)

def areaOf(s, x): # begin here
    cA = circle(x)
    sA = square(x)
    eA = equilateralTriangle(x)
    print("the area of the circle = ", cA)
    print("the area of the square = ", sA)
    print("the area of the equilateral triangle = ", eA)

print(areaOf(s, x))
