import tkinter

window = tkinter.Tk()
window.title("My First GUI program in Python")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)


#label
my_label = tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Button
def button_clicked():
    txt = input.get()  
    my_label.config(text=txt)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)

button2 = tkinter.Button(text="Click Me", command=button_clicked)
button2.grid(column=1, row=1)

#Entry
#Docs: http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
#input.pack()



window.mainloop()