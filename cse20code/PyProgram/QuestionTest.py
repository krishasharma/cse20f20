#QuestionTest.py

print("\n\nEnter two numbers, low then high.") #asking user to enter low and high
low=int(input("low = "))
high=int(input("high = "))

while(low>high): #asking user repeatedly until valid low and high are entered
    print("\nPlease enter the smaller followed by the larger number.")
    low=int(input("low = "))
    high=int(input("high = "))
print("\nThink of a number in the range %d to %d."%(low, high))

if(low==high):#printing the result if low is equal to high
    print("\nYour number is %d. I found it in 0 guesses.\n\n"%(low))
    exit()

count=0
mid=(high+low)//2 #calculating middle value
choices=['L', 'G', 'E', 'l', 'g', 'e'] #initializing the list of valid choices

print("\nIs your number Less than, Greater than, or Equal to %d?"%(mid)) #asking user for less than, greater than or equal to choice
choice=input("Type 'L', 'G' or 'E': ")

while(choice not in choices): #asking user repeatedly until valid choice is entered
    choice=input("\nPlease type 'L', 'G' or 'E': ")

count+=1 #incrementing guess everytime user is asked for choice

if(choice=='e' or choice=='E'):#if user enters E, printing result
    print("\nI found your number in 1 guess.\n\n")

while(choice!='e' and choice!='E'): #looping until result is found
    #if user enters L, setting high one less than m
    if(choice=='l' or choice=='L'):
        high=m-1
    #if user enters G, setting low one greater than m
    elif(choice=='g' or choice=='G'):
        low=mid+1
    #printing the result if low is equal to high
    if(high==low):
        print("\nYour number is %d. I found it in %d guesses.\n\n"%(low, count))
        break
    #if count == 1:
           # print("I found your number in 1 guess.")
           # break
        #else:
            #print("I found your number in ",count," guesses.")
            #break
    if(high<low):
        print("\nYour answers have not been consistent.")
        break
    
    mid=(high+low)//2 #calculating mid 
    print("\nIs your number Less than, Greater than, or Equal to %d?"%(mid)) #asking user for less than, greater than or equal to choice again
    choice=input("Type 'L', 'G' or 'E': ")
   
    while(choice not in choices):  #asking user repeatedly until valid choice is entered
        choice=input("\nPlease type 'L', 'G' or 'E': ")
   
    count+=1  #incrementing guess
    if(choice=='e' or choice=='E'): #if user enters E, printing result
        print("\nI found your number in %d guesses.\n\n"%(count))




