#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 3 
#The purpose of this program is to compute the surface area and volume of a cylinder and sphere using user inputed values. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Formulas.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import math

#start functions for the formulas for SA and V of cylinder and sphere 

#start sphere_volume 
def sphere_volume(r):
    sV = (4/3)*math.pi*pow(r,3)
    return sV 
#end sphere_volume

#start sphere_area
def sphere_area(r):
    sA = 4*math.pi*pow(r,2)
    return sA
#end spher_area 

#start cylinder_volume
def cylinder_volume(r, h):
    cV = math.pi*pow(r, 2)*h
    return cV
#end cylinder_volume 
    
#start cylinder_area 
def cylinder_area(r, h):
    cA = 2*math.pi*pow(r, 2)+2*math.pi*r*h
    return cA
#end cylinder_area 

#end formulas for SA and V of cylinder and sphere
 
#start print fucntions 

#start print_sphere
def print_sphere(r):
    sV = sphere_volume(r) 
    sA = sphere_area(r)
    print("The volume of the sphere with radius", r, "is:", sV)
    print("The surface area of the sphere with radius", r, "is:", sA)
#end print_sphere

#start print_cylinder
def print_cylinder(r, h):
    cV = cylinder_volume(r, h)
    cA = cylinder_area(r, h)
    print("The volume of the cylinder with radius", r, "and height", h, "is:", cV)
    print("The surface area of the cylinder with radius", r, "and height", h, "is:", cA)
#end print_cylinder 

#end print functions 

#--main program------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Enter three numbers:")
first = float(input("first number: "))
second = float(input("second number: "))
third = float(input("third number: "))
print() #blank line 

#print commands 
print_sphere(first)
print()
print_sphere(second)
print()
print_sphere(third)
print()
print_cylinder(first, second)
print()
print_cylinder(second, third)
print()
print_cylinder(third, first)
print()

#end program----------------------------------------------------------------------------------------------------------------------------------------------------------------
