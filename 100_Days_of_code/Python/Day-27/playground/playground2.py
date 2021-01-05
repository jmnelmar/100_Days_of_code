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

