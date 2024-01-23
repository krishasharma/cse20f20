#------------------------------------------------------------------------------
# TwentyQuestions.py
#------------------------------------------------------------------------------

import random    
limit = 1000000             
number = random.randint(1, limit)

num_guesses = 0
msg = ""

while True:
   guess = int(input(msg + "\nGuess my number between 1 and "+str(limit)+" : " ))
   num_guesses += 1
   if guess > number:
      msg += str(guess) + " is too high.\n"
   elif guess < number:
      msg += str(guess) + " is too low.\n"
   else:
      break
   # end if-elif-else
# end while

print("\n\nGreat, you got it in {0} guesses!\n\n".format(num_guesses))

#same as
#print("\n\nGreat, you got it in "+str(num_guesses)+" guesses!\n\n")