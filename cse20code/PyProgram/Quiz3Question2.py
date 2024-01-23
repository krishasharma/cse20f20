#Krisha Sharma 
#Quiz 3 Question 2

import random 
#def rotate(L, i, j, k):
    #return l[i:] + l[:]

def rotate(L, i, j, k): 
    temp = L[i]
    L[i] = L[j]
    L[j] = L[k]
    L[k] = temp
    return

# end swap()

# main program ----------------------------------
L = ["one", "two", "three", "four"]

print(L) #[‘one’, ‘two’, ‘three’]
rotate(L, 0, 3, 5)
print(L) # [‘three’, ‘two’, ‘one]
