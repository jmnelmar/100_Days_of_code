FONT = ("Courier", 12, "normal")
ALIGMENT = "left"
LEVEL_POSITION = (-280,280)

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.print_level()

    def print_level(self):
        self.clear()
        self.goto(LEVEL_POSITION)
        self.write(f"Level: {self.level}",move=False, align=ALIGMENT, font=FONT)
        
    def print_game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!",move=False, align=ALIGMENT, font=FONT)