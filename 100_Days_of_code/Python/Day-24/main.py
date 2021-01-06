from snake import Snake
from food import Food
from scoreboard import ScoreBoard

from turtle import Screen
import time

def set_screen(scr, snk):
    scr.setup(width=600,height =600)
    scr.bgcolor("black")
    scr.title("My Snake Game")
    scr.tracer(0)
    scr.listen()
    scr.onkey(snk.up, "Up")
    scr.onkey(snk.down, "Down")
    scr.onkey(snk.left, "Left")
    scr.onkey(snk.right, "Right")
    
screen = Screen()
snake = Snake()
set_screen(screen, snake)
food = Food()
score = ScoreBoard()

with open("high_score.txt") as file:
    score.high_score = int(file.read())
    score.refresh(1) 


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
        #snake.game_is_on = False
        score.game_over()
        time.sleep(2)
        screen.clear()
        set_screen(screen, snake)
        snake.reset()
        food = Food()
        if score.score > score.high_score:
            score.high_score = score.score
            score.score = 0
            with open("high_score.txt", mode="w") as file:
                file.write(str(score.high_score))
        else:
            score.score = 0
        score.refresh(0)
    
    #Detect collision with tail
    for segment in snake.segments[1:]:
        #if segment == snake.head():
        #    pass
        #el
        if snake.head().distance(segment) < 10:
            snake.game_is_on = False
            score.game_over()

screen.exitonclick()