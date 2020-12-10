import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
def set_pen(tim):
  tim.penup()
  tim.backward(50)
  tim.right(-90)
  tim.forward(150)
  tim.left(-90)
  tim.pendown()

def change_color(tim):
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

set_pen(tim)
for i in range( 3, 11):
  angle = (360/i) * -1
  change_color(tim)
  for j in range( 1, i+1):
    tim.forward(100)
    tim.left(angle)
