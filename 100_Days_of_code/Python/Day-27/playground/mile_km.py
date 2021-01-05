from tkinter import *

def calculate():
    value = (int)(entry.get())
    label3["text"] = value * 1.6
    print("Calculate!")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100,width=280)
window.config(padx=20,pady=20)

label = Label()
label.config(text="is equal to")
label.grid(column=0,row=1)
label.config(padx=5,pady=5)

entry = Entry(width=10)
entry.grid(column=1,row=0)
#entry.config(padx=5, pady=5)

label2 = Label(text="Miles")
label2.grid(column=2,row=0)
label2.config(padx=5, pady=5)

label3 = Label()
label3.config(text="0",padx=5, pady=5)
label3.grid(column=1,row=1)

label4 = Label()
label4.config(text="Km",padx=5, pady=5)
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate, padx=5, pady=5)
button.grid(column=1,row=2)


window.mainloop()