import turtle
import pandas
from pandas.core.indexing import convert_to_index_sliceable
from board import Board

FONT = ("Courier", 12, "normal")
ALIGMENT = "left"
LEVEL_POSITION = (-280,280)

#screen = turtle.Screen()
#screen.title("U.S States Game")
##image = "blank_states_img.gif"
#screen.addshape(image)
#turtle.shape(image)
answer = ""
br = Board()


def get_mouse_click_coor(x,y):
    answer = br.screen.textinput(title=f"Guess the State{br.points}/50", prompt="What's another state's name?")
    data = pandas.read_csv("50_states.csv")
    serie = data[ data.state == answer ]   
    print(serie) 
    if not serie.empty:
        points = br.points +1
        corx =  int(serie.x) 
        cory = int(serie.y)
        state = serie.values[0][0] 
        br.write_on_board(corx,cory,state)     
    else:
        print("not ok")
           
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


#screen.exitonclick()

#-327.0 114.0, -282.0 100.0

#-278.0 -56.0, -242.0 -45.0, 