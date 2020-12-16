from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, xcor = 0, ycor = 0):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.score = 0
        self.y_speed = 50
        self.goto(xcor,ycor)
    
    def go_up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor() + self.y_speed)

    def go_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - self.y_speed )
