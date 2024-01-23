#!/usr/local/bin/python3
import sys
height = int(float(sys.argv[1]))
width = int(float(sys.argv[2]))
temp = 2 * (width - 2)
for i in range(1, height+1):
    if i == 1 or i == height:
        print("+", end="")
    else:
        print("|", end="")
    for j in range(temp):
        if i == 1 or i == height:
            print("-", end="")
        else:
            print(" ", end="")
    if i == 1 or i == height:
        print("+")
    else:
        print("|")