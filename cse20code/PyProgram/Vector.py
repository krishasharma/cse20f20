#------------------------------------------------------------------------------
# Vector.py
#------------------------------------------------------------------------------
"""
This module provides functions to perform standard vector operations.  Vectors
are represented as tuples of numbers (floats or ints).  Functions that take two 
vector arguments will raise a ValueError() exception if the two vectors are of
different dimensions.  
"""
#------------------------------------------------------------------------------
# import library modules
#------------------------------------------------------------------------------
import math 
import random 

#------------------------------------------------------------------------------
# function definitions
#------------------------------------------------------------------------------

# add() ----------------------------------------------------------------------- 
def add(u, v): #sum of u+v
    "Return the vector sum u+v."
    add=[] 
    if not len(u) == len(v): 
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    for k in range(len(u)):
         add.append(u[k]+v[k]) 
    return tuple(add) 
# end add() -------------------------------------------------------------------


# negate() --------------------------------------------------------------------
def negate(u): #-u of u 
    "Return the negative of the vector u."
    negate=[] 
    for k in range(len(u)):
        negate.append(-1*u[k]) 
    return tuple(negate) 
# end negate() ----------------------------------------------------------------   


# sub() -----------------------------------------------------------------------
def sub(u, v): #difference of u-v
    "Return the vector difference u-v."
    if not len(u) == len(v):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    return add(u,negate(v))
# end sub() -------------------------------------------------------------------


# scalarMult() ----------------------------------------------------------------
def scalarMult(c, u):
    "Return the scalar product cu of the number c by the vector u."
    scalarMult=[] 
    for k in range(len(u)):
         scalarMult.append(c*u[k]) 
    return tuple(scalarMult) 
# end scalarMult() ------------------------------------------------------------


# hadamard() ------------------------------------------------------------------
def hadamard(u, v):
    "Return the Hadamard product of u with v."
    hadamard=[]
    if not len(u) == len(v):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    for k in range(len(u)):
         hadamard.append(u[k]*v[k]) 
    return tuple(hadamard) 
# end hadamard() --------------------------------------------------------------


# dot() -----------------------------------------------------------------------
def dot(u, v):
    "Return the dot product of u with v."
    if not len(u) == len(v):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    a = u[:]
    b = v[:]
    c = hadamard(a,b)
    dot = 0 
    for k in range(len(c)):
        dot+= c[k]
    return dot 
# end dot() -------------------------------------------------------------------


# length() --------------------------------------------------------------------
def length(u):
    "Return the (geometric) length of the vector u."
    length=0 
    for k in range(len(u)):
         length+=(u[k]*u[k])  
    return math.sqrt(length) 
# end length() ----------------------------------------------------------------


# dim() -----------------------------------------------------------------------
def dim(u):
    "Return the dimension of the vector u."
    return len(u) 
# end dim() -------------------------------------------------------------------


# unit() ----------------------------------------------------------------------
def unit(v):
    "Return a unit (geometric length 1) vector in the direction of v."
    return tuple(scalarMult(1/length(v),v))
# end unit() ------------------------------------------------------------------


# angle() ---------------------------------------------------------------------
def angle(u, v):
    "Return the angle (in radians) between vectors u and v."
    if not len(u) == len(v):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    return math.acos(dot(unit(u),unit(v)))
# end angle() -----------------------------------------------------------------


# randVector() ----------------------------------------------------------------
def randVector(n, a, b):
    """Return a vector of dimension n whose components are random floats in
    the range [a, b)."""
    randVector = [] 
    for k in range(n):
        randVector.append(random.uniform(a,b)) 
    return tuple(randVector) 
# end randomVector() ----------------------------------------------------------

if __name__ == '__main__':
    print()
    """DESCRIPTION
            This module provides functions to perform standard vector operations.  Vectors
            are represented as tuples of numbers (floats or ints).  Functions that take two 
            vector arguments will raise a ValueError() exception if the two vectors are of
            different dimensions."""