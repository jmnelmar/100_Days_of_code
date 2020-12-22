import turtle
import pandas
from pandas.core.indexing import convert_to_index_sliceable

FONT = ("Courier", 12, "normal")
ALIGMENT = "left"
LEVEL_POSITION = (-280,280)

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer = ""
points = 0
is_game_on = True


def print_name(x,y,state):
    pen = turtle.Turtle()
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(x,y)
    pen.write(state)


def get_mouse_click_coor(x,y):
    answer = screen.textinput(title=f"Guess the State{points}/50", prompt="What's another state's name?")
    #data = pandas.read_csv("50_states.csv")
    #serie = data[ data.state == answer ]
    #print("state: "+serie["state"]+", x: "+str(serie["x"]) +", y: "+str(serie["y"])) 

    data = pandas.read_csv("50_states.csv")
    serie = data[ str(data.state).lower() == answer.lower() ]
    
    
    if not serie.empty:
        points = points +1
        corx =  int(serie.x) 
        cory = int(serie.y)
        state = serie.values[0][0] 
        print_name(corx,cory,state)     
    else:
        print("not ok")
        points = points

    


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


#screen.exitonclick()

#-327.0 114.0, -282.0 100.0

#-278.0 -56.0, -242.0 -45.0, 