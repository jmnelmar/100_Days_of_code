from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.update()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
ball = Ball(0,0)


score = Score()

while game_is_on:  
    game_is_on = ball.collisions([l_paddle, r_paddle], score)
    time.sleep(0.01)
    ball.goto(ball.xcor()+ball.x_speed, ball.ycor()+ball.y_speed)
    screen.update()
    score.print_score();
score.print_game_over()
screen.exitonclick()


# Things to do.
# Create the screen - Done.
# Create and move the paddle - Done.
# Create another paddle - Done.
# Create the ball and make it move - Done.
# Detect collision with wall and bounce - Done
# Detect collision with paddle -Done
# Detect when paddle misses - Done
# Keep Score - Done