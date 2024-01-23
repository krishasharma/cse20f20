#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 7 
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Probability.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random

def throwDice(m, k, R):
    R = random.Random(237)
    tup = []
    for dice in range(m):
        tup.append(random.randrange(1, k+1))
    return tuple(tup)

#main code 
def main(SEED=237):
    random.seed(237)
    dic = int(input('Enter the number of dice: '))
    while dic<=0:
        if dic<=0: 
            print('\nThe number of dice must be at least 1')
            dic=int(input('Please enter the number of dice: \n'))
        sid=int(input('\nEnter the number of sides on each die: \n'))
    while sid<=1:
        if sid<=1: print('The number of sides on each die must be at least 2')
        sid=int(input('Please enter the number of sides on each die: '))
    frequency = [0] * (dic*sid + 1) #declaring list
    tri=int(input('\nEnter the number of trials to perform: \n')) 
    while tri<=0:
        if tri<=0:print('The number of trials must be at least 1')
        tri=int(input('Please enter the number of trials to perform: '))
    dic = int(input("Please enter the number of dice: "))
    sid = int(input("\nEnter the number of sides on each die: ")) #input from user
    tri = int(input("\nEnter the number of trials to perform: ")) #input from user 
    R = random.seed(237)
    for _ in range(tri): #finds the frequency 
        dice_values = throwDice(dic, sid, R)
        i = sum(list(dice_values))
        frequency[i] += 1
    print("\n Sum Frequency Relative Frequency Experimental Probability") #results 
    print("-" * 70)
    for i in range(dic,len(frequency)):
        relativeFreq = frequency[i]/tri #relative frequency and experimental probability
        experimentalProb = relativeFreq * 100
        print("{:4d}{:11d}{:18.5f}{:21.2f} %".format(i,frequency[i],relativeFreq, experimentalProb))

if __name__=='__main__':
    main(SEED=237)


#m= dic
#k= sid
#n= tri


