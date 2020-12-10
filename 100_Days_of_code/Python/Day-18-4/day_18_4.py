import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def change_color(tim):
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

tim.width(5)
for i in range (1,100):
  angle = random.randint(1,4) * 90
  tim.left(angle)
  tim.color( colours[random.randint(0,7)] )
  #change_color(tim)
  tim.forward(30)