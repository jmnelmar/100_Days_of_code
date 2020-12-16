from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courrier", 30, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0,250)
        self.write(f"{self.score}:{self.score2}", move=True, align=ALIGMENT, font=FONT)
    

    def print_game_over(self):
        self.goto(0,100)
        self.write(f"Game set! final score {self.score}:{self.score2}", move=True, align=ALIGMENT, font=FONT)