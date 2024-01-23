#Winding.py

import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.color('blue','green')
t.pensize(3)

t.penup()
t.setpos(0,-150)
t.pendown()

t.begin_fill()

t.circle(200)
t.circle(160)
t.circle(120)
t.circle(80)
t.circle(40)

t.end_fill()

wn.mainloop()