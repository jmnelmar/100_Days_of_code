from snake import Snake
from food import Food
from scoreboard import ScoreBoard

from turtle import Screen
import time

screen = Screen()
screen.setup(width=600,height =600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while snake.game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect collision with food.
    if snake.head().distance(food) < 15:
        food.refresh()
        score.refresh(1)
        snake.extend( )

    #Detect collision with the wall
    if snake.head().xcor() > 280 or snake.head().xcor() < -280 or snake.head().ycor() > 280 or snake.head().ycor() < -280:
        snake.game_is_on = False
        score.game_over()
    
    #Detect collision with tail
    for segment in snake.segments[1:]:
        #if segment == snake.head():
        #    pass
        #el
        if snake.head().distance(segment) < 10:
            snake.game_is_on = False
            score.game_over()

screen.exitonclick()