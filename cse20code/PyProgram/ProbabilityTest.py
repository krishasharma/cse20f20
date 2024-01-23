import random

def throwDice(m, k, R): #function throwDice()
    R = random.Random(237)
    tup = []
    for _ in range(m):
        tup.append(random.randrange(1,k+1))
    return tuple(tup)

#main program 
def main(SEED=237):
    random.seed(237)
    m = int(input("\nEnter the number of dice: ")) #input from user
    while m<1:
        print("The number of dice must be at least 1")
        m = int(input("Please enter the number of dice: ")) #input from user 
    k = int(input("\nEnter the number of sides on each die: ")) #input from user
    while k<2:
        print("The number of sides on each die must be at least 2")
        k = int(input("Please enter the number of sides on each die: ")) #input from user 
    n = int(input("\nEnter the number of trials to perform: ")) #input from user 
    while n<1:
        print("The number of trials to perform must be at least 1")
        n = int(input("Please enter the number of trials to perform: "))
m = int(input("Please enter the number of dice: "))
k = int(input("\nEnter the number of sides on each die: ")) #input from user
n = int(input("\nEnter the number of trials to perform: ")) #input from user 
R = random.seed(237)
frequency = [0] * (m*k + 1) #declaring list 
for _ in range(n): #finds the frequency 
    dice_values = throwDice(m, k, R)
    i = sum(list(dice_values))
    frequency[i] += 1
print("\n Sum Frequency Relative Frequency Experimental Probability") #results 
print("-" * 70)
for i in range(m,len(frequency)):
    relativeFreq = frequency[i]/n #relative frequency and experimental probability
    experimentalProb = relativeFreq * 100
    print("{:4d}{:11d}{:18.5f}{:21.2f} %".format(i,frequency[i],relativeFreq, experimentalProb))

if __name__=='__main__':
    main(SEED=237)



