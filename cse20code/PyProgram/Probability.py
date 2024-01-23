#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 7 
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Probability.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random
#throwDice()
def throwDice(m, k, R):
    R = random.Random(237)
    tup = []
    for dice in range(m): 
        tup.append(random.randrange(1, k+1))
    return tuple(tup)
#main
def main(SEED=237):
    random.seed(237)
    m = int(input("\nEnter the number of dice: "))
    while m<1: 
        print("The number of dice must be at least 1")
        m = int(input("Please enter the number of dice: "))
    k = int(input("\nEnter the number of sides on each die: "))
    while k<2:
        print("The number of sides on each die must be at least 2")
        k = int(input("Please enter the number of sides on each die: "))
    n = int(input("\nEnter the number of trials to perform: "))
    while n<1:
        print("The number of trials must be at least 1")
        n = int(input("Please enter the number of trials to perform: "))
    R = random.seed(237)
    frequency = (m*k + 1)*[0]  
    for _ in range(n):
        dV = throwDice(m, k, R)
        i = sum(list(dV))
        frequency[i] += 1
    print("\n Sum     Frequency     Relative Frequency     Experimental Probability")
    print("-" * 70)
    for i in range(m,len(frequency)):
        relativeFrequency = frequency[i]/n
        experimentalProbability = relativeFrequency * 100
        print("{:4d}{:11d}{:18.5f}{:21.2f} %".format(i,frequency[i],relativeFrequency, experimentalProbability))
    print("")
#end main
if __name__=='__main__':
    main(SEED=237)