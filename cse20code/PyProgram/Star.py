#Star.py 
#Krisha Sharma (1797229)
#krvsharm@ucsc.edu
#CSE-20-02 pa2
#this program creates an n-pointed star, where n is a user inputed odd integer that is greater than or equal to 3. 

import turtle
n = int(input('Enter any odd integer greater than or equal to 3: '))
d = 300
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("white")
wn.title(str(n)+" pointed star") #title for window that change with user input 

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("blue", "green")
tess.pensize(2)
tess.penup()
tess.setpos(-150,0) #setting position of turtle to a certain coordinate
tess.pendown()

#start drawing n-pointed star 

angle=180.0-180.0/n

tess.speed(0) #makes animation as fast as possible; should i use turtle tracer instead?

tess.begin_fill()

for i in range(n):
    tess.forward(d)
    tess.right(angle)
    tess.dot(10, "red")  #creates red dot at the end of the points 

tess.end_fill()

tess.hideturtle()
wn.mainloop()

#turtle.forward(300) #used to draw a line, used after setpos()
#turtle.dot(10, "red") #red dot with diameter of 10px
#set position at -150,0 before starting, then go 300 pixles to the right ending at 150,0
#turtle should be hidden after the program runs