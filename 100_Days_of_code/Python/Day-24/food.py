from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.colors = ["blue","red","yellow","purple","white","green"]
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(self.colors[random.randint(0, len(self.colors)-1)])
        self.goto(random.randint(-260, 260), random.randint(-26, 260))