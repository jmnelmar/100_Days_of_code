from turtle import Turtle
import time

class Ball(Turtle):
    
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_speed = 0.5
        self.y_speed = 0.5
        self.goto(xcor, ycor)

    def collisions(self, paddles, score):
        game_is_on = True
        if self.ycor() > 280:
            self.y_speed *= -1 
        elif self.ycor() < -280:
            self.y_speed = abs(self.y_speed)
        else:
            for paddle in paddles:
                if abs(self.xcor() - paddle.xcor()) < 20 and abs(self.ycor() - paddle.ycor()) < 80:
                    if paddle.xcor() > 0:
                        self.x_speed *= -1
                        self.x_speed -= 0.1     
                    else:
                        self.x_speed = abs(self.x_speed)
                        self.x_speed += 0.1

        if self.xcor() > 375:
            score.score += 1 
            self.goto(0,0)
            self.x_speed = 0.5
            self.y_speed = 0.5
            time.sleep(1)
        elif self.xcor() < -375:
            score.score2 += 1
            self.goto(0,0)
            self.x_speed = 0.5
            self.y_speed = 0.5
            time.sleep(1)
        if score.score >= 10 or score.score2 >= 10:
            game_is_on = False
        return game_is_on

        