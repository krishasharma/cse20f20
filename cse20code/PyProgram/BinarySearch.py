#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 6 
#
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#BinarySearch.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n\nEnter two numbers, low then high.")
low = int(input("low = "))
high = int(input("high = "))

while(low>high):
    print("\nPlease enter the smaller followed by the larger number.")
    low = int(input("low = "))
    high = int(input("high = "))

print("\nThink of a number in the range %d to %d."%(low,high))

if(low==high):
    print("\nYour number is %d. I found it in 0 guesses.\n\n"%(low))
    exit()
guess = 0 

m=(high+low)//2

choices=['L', 'G', 'E', 'l', 'g', 'e']

print("\nIs your number Less than, Greater than, or Equal to %d?"%(m))
choice=input("Type 'L', 'G' or 'E': ")

while(choice not in choices):
    choice=input("\nPlease type 'L', 'G' or 'E': ")
guess+=1

if(choice=='e' or choice=='E'):
    print("\nI found your number in 1 guess.\n\n")

while(choice!='e' and choice!='E'):
    
    if(choice=='l' or choice=='L'):
        high=m-1

    elif(choice=='g' or choice=='G'):
        low=m+1

    if(high==low):
        print("\nYour number is %d. I found it in %d guesses.\n\n"%(low, guess))
        break

    if(high<low):
        print("\nYour answers have not been consistent.\n\n")
        break

    m=(high+low)//2

    print("\nIs your number Less than, Greater than, or Equal to %d?"%(m))
    choice=input("Type 'L', 'G' or 'E': ")
    
    while(choice not in choices):
        choice=input("\nPlease type 'L', 'G' or 'E': ")
    guess+=1

    if(choice=='e' or choice=='E'):
        print("\nI found your number in %d guesses.\n\n"%(guess))

#-------------------------------------------------------------------------------------------------------------------------------------


print("\n\nEnter two numbers, low then high.")
low = int(input("low = "))
high = int(input("high = "))

while low>high:
    print("\nPlease enter the smaller followed by the larger number.")
    low = int(input("low = "))
    high = int(input("high = "))
    if low<=high:
        break

print("\nThink of a number in the range %d to %d."%(low, high))
count = 0


while low<=high:
    mid = (low+high)//2
    ch = input("Type 'L', 'G' or 'E': ")
    count = count+1
    if low == high:
        print("\nYour number is %d. I found it in %d guesses.\n\n"%(low, count))
        break
    print("\nIs your number Less than, Greater than, or Equal to %d?"%(mid))
    #if user does types something other than L, G, E, l, g, e, program returns "please type..."
    while ch != "L" and ch != "l" and ch != "G" and ch != "g" and ch !='E' and ch != 'e':  
        ch = input("\nPlease type 'L', 'G' or 'E': ")
        if ch == "L" or ch == "l" or ch == "G" or ch == "g" or ch =='E' or ch == 'e':
            break
    if ch == "E" or ch =='e':
        if count == 1:
            print("\nI found your number in 1 guess.\n\n")
            break
        else:
            print("\nI found your number in %d guesses.\n\n"%(count))
            break
    elif ch == "G" or ch == "g":
        low = mid+1
    elif ch == "L" or ch == "l":
        high = mid-1

if choice == 'G' or choice == 'g' and high == low+1 and count == 1: #added
    print("\nYour number is %d. I found it in %d guess.\n\n"%(high, count))
    exit()

if low > high:
    print("\nYour answers have not been consistent.\n\n")