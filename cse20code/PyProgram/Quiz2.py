import turtle
import math 
wn = turtle.Screen()
alice = turtle.Turtle()
bob = turtle.Turtle()

side = 100
turn_angle = 90

#code starts here
alice.color("red")
bob.color("blue")
alice.pensize(2)
bob.pensize(2)
alice.penup()
alice.setpos(0,0) #setting position of turtle to a certain coordinate
alice.pendown()
bob.penup()
bob.setpos(0,0)
bob.pendown()

#alice drawing the square 
for i in range(4):
    alice.forward(side)
    alice.left(turn_angle)

#bob drawing the diagnoal line 
bob.left(0.5*turn_angle) #45 degree angle
bob.forward(250) #line 250
#code ends here

wn.mainloop()