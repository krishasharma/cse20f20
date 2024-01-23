#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 5 
#The purpose of this program is to list all the prime numbers that are less than or equal n from user input.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Sieve.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def makeSieve(n): #create a boolean array S[0..n] and initialize all entries as true
    S = [True for i in range(n+1)] 
    i = 2
    while (i**2 <= n): #if S[i] is not a multiple of the previous prime, then it is a prime 
        if (S[i] == True): #update all multiples of i 
            for j in range(i*2, n+1, i): 
                S[j] = False
        i += 1
    S[0]= False 
    S[1]= False 
    return S

def getPrimes(n):
    seive=makeSieve(n) #calling makeSieve()
    P=[] #empty list to store primes
    for i in range(2,len(seive)):  #checking all the values which are true in seive and adding them to P
        if seive[i]==True:
            P.append(i)
    return P
    
#main program code 

n = int(input("Enter a positive integer: "))
while n <=0:
    n = int(input("Please enter a positive integer: "))

S = makeSieve(n) #calling fucntion 
P = getPrimes(n) #calling fucntions that return a list of prime numbers 
print("")
print("There are "+str(len(primes))+" prime numbers less than or equal to "+str(n)+":")
print("")

for i in range(len(P)):
    print(P[i],end=" ")
    if (i+1) % 10==0:
        print("")

print("")
print("")
