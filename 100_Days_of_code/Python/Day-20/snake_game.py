from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height =600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = []

def make_body():
    for i in range(1, 4):
        body = Turtle()
        body.shape("square")
        # body.shapesize(20,20)
        body.penup()
        body.color("white")
        body.goto(x=-40+20*i, y = body.ycor())
        snake.append(body)

make_body()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(snake)-1, 0, -1):
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num-1].ycor()
        snake[seg_num].goto(new_x, new_y)
    
    snake[0].forward(20)
    snake[0].left(90)
    #for body in snake:
    #    body.forward(20)
        

screen.exitonclick()