def add(*args):
    response = 0
    for arg in args:
        response += (int)(arg)
    return response

print(add(1,2,3,4,5,6,100))

def calculate(n,**kwargs):
    print(kwargs)

    #for key,value in kwargs.items():
    #    print(key)
    #    print(value)
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")#si no existe devuelve None


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)

my_car = Car(make="Nissan")
print(my_car.model)

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program in python")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold"))
#my_label.pack(side="left")#
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="Click Count")

click = 0

#Entry
#Docs: http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input = tkinter.Entry(width=10)
input.pack()

def button_clicked():
    txt = input.get()  
    my_label.config(text=txt)


#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()







window.mainloop()

