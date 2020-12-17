import time
from turtle import Screen
import turtle
from player import Player
from scoreboard import Scoreboard
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
level = Scoreboard()
car_manager = CarManager() 


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    level.print_level()
    car_manager.move_cars()
    game_is_on = not car_manager.collision(player)
    if player.ycor() >= FINISH_LINE_Y:
        player.reset()
        level.level += 1
        car_manager.increase_speed()
    screen.update()

level.print_game_over()

screen.exitonclick()
