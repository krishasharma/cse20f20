#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 6 
#This program takes user inputed numbers for "low" and "high" and guesses a number that the user chose in a rannge decided by "high" and "low".
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Question.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n\nEnter two numbers, low then high.")
low = int(input("low = "))
high = int(input("high = "))

while(low>high):
    print("\nPlease enter the smaller followed by the larger number.")
    low = int(input("low = "))
    high = int(input("high = "))

print("\nThink of a number in the range %d to %d."%(low,high))
if low == high: #low number is being compared to high value, if they low is equal to high it will return that it was found in 0 guesses
    print("\nYour number is %d. I found it in 0 guesses.\n\n"%(low))
    exit()
count = 0 #setting the count equal to 0, the number of guesses
mid = (high+low)//2 #this finds the middle of the range in the set of numbers in between the low and high inputs 
chs = ['L', 'G', 'E', 'l', 'g', 'e'] #list of users input choices to respond when asked about less than, greater than or equal to
print("\nIs your number Less than, Greater than, or Equal to %d?"%(mid))
ch = input("Type 'L', 'G' or 'E': ")

while ch not in chs:
    ch = input("\nPlease type 'L', 'G' or 'E': ")
count += 1

if ch == 'e' or ch == 'E':
    print("\nI found your number in 1 guess.\n\n")

if ch == 'g' or ch == 'G' and count == 1 and high == low+1: #when a choice is greater than the number thats been guessed  
    print("\nYour number is %d. I found it in %d guess.\n\n"%(high, count))
    exit()

while ch != 'e' and ch != 'E':
    if ch == 'l' or ch == 'L':
        high = mid-1
    elif ch == 'g' or ch == 'G':
        low = mid+1
    if high == low:
        print("\nYour number is %d. I found it in %d guesses.\n\n"%(low, count))
        break
    if high<low:
        print("\nYour answers have not been consistent.\n\n")
        break
    mid = (high+low)//2 #calculates the middle value 
    print("\nIs your number Less than, Greater than, or Equal to %d?"%(mid))
    ch = input("Type 'L', 'G' or 'E': ")
    while ch not in chs: #keeps asking the user to enter a vaild entry 
        ch=input("\nPlease type 'L', 'G' or 'E': ")
    count += 1 #incrementing the guesses by 1 each time a guess occours 
    if ch == 'e' or ch == 'E':
        print("\nI found your number in %d guesses.\n\n"%(count))

