import tkinter

window = tkinter.Tk()
window.title("My First GUI program in Python")
window.minsize(width=500, height=300)

#label

my_label = tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack(side="left", expand=True)







window.mainloop()