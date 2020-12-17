COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        #self.hideturtle()
        self.shapesize(stretch_len=2, stretch_wid=1, outline=None)
        self.color( COLORS[random.randint(0,5)] )
        self.goto(random.randint(-280,280) , random.randint(-260,280) )
        self.speed = STARTING_MOVE_DISTANCE

    def set_cor(self):
        self.goto(300 , random.randint(-260,280) )

    def move(self):
        self.goto(self.xcor()-self.speed, self.ycor())

    def detect_collision(self, t):
        colision = False
        if abs(self.xcor() - t.xcor()) < 30 and abs(self.ycor() - t.ycor()) < 19:
            colision = True
        return colision