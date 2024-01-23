#Module.py

import math 
import random 

def class Vector:
    def __init__(self, a, b):
        self.xcomp = a
        self.ycomp = b
    # end __init__()

    def __str__(self):
        return '('+str(self.xcomp)+', '+str(self.ycomp)+')'
    # end __str__()

    def dot(self, other):
        # begin here
        a = self[:]
        b = other[:]
        c = hadamard(a,b)
        dot = 0 
        for k in range(len(c)):
            dot+= c[k]
        return dot 
        # end dot()

    def add(self, other):
        # begin here
        add=[] 
        for k in range(len(self)):
            add.append(self[k]+other[k]) 
        return tuple(add) 
        # end add()
# end class Vector

