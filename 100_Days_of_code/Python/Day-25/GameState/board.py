from turtle import Turtle, Screen
import pandas

FONT = ("Courier", 12, "normal")
ALIGMENT = "left"
LEVEL_POSITION = (-280,280)

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.pen = Turtle()
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()
        self.screen = Screen()
        self.screen.title("U.S States Game")
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        self.shape(self.image)

        
        
        
    def write_on_board(self ,x, y, txt):    
        self.pen.goto(x,y)
        self.pen.write(txt)
