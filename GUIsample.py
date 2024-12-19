from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("Samuel Joseph")
window.configure(bg="red")

def hello():
    print("Button clicked")




button1=Button(text="ok", command=hello)
button2=Button(text="ok", command=hello)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)

window.mainloop()
print("Heyyy")