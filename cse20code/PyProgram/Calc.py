#!/usr/local/bin/python3

from math import *
import sys
A = list()
if len(sys.argv) > 1:
        A.append(eval("".join(sys.argv[1:])))
        print(eval("".join(sys.argv[1:])))
else:
    i = 0
    while True:
        u_input = input("A[{}]:= ".format(i))
        if u_input == "":
            print()
            break
        A.append(eval(u_input))
        print(eval(u_input))
        i += 1