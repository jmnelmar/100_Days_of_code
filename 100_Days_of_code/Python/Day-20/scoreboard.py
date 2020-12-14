from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 12, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.print_score()

    def refresh(self, number):
        self.clear()
        self.score += number
        self.print_score()

    def print_score(self):
        self.goto(0,270)
        self.write(f"Score: {self.score}", move=True, align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", move=True, align=ALIGMENT, font=FONT)