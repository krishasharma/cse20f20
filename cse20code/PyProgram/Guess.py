#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Krisha Sharma 
#krvsharm@ucsc.edu
#Programming Assingment 4 
#The purpose of this program is to have the user guess a random integer within the range 1-10. The user will have 3 chances to guess the number. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Guess.py 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random

n = random.randint(1, 10) #sets range between 1-10

guess_limit = 2 #actual count will be 3

guess_count = 0 #index

guess_list = ["first", "second", "third"]

print()
print("I'm thinking of an integer in the range 1 to 10. You have three guesses.")
print()

while guess_count <= guess_limit:
    guess = int(input("Enter your " + guess_list[guess_count] + " guess: ")) #guess_list[guess_count] is what changes first/second/third
    guess_count += 1 #increases guess counter by 1 every time a guess is made 
    if guess == n: #if the guess is equal to the random number
        print("You win!") #print "You win!"
        print()
        break #stops loop 

    elif guess > n: #if guess is greater than the random number
      print("Your guess is too high.") #print "Your guess too high"
      print()  

    elif guess < n: #if guess is less than the random number 
      print("Your guess is too low.") #print "your guess is too low"
      print()

else: #if user cannot guess the random number in 3 tries  
    print("You lose. The number was {}.".format(n)) #print "You loose." and tell them what the number was
    print()


