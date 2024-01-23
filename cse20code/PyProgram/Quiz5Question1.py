#Quiz5Question1

import math

n = int(input("Enter value for n: "))

def squares(n):
    number = []
    for i in range (1,n+1):
        number.append(pow(i,2)) 
    return number

print(squares(n))

