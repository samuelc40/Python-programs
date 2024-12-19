from tkinter import *
import tkinter.messagebox
root = Tk()

def save():
    print("Project saved...")

def exit():
    tkinter.messagebox.askyesno("Quit", "You sure you want to exit?")
    quit()

mymenu = Menu(root)
root.config(menu = mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Save", command=save)
submenu.add_separator()
submenu.add_command(label="Exit", command=exit)

newmenu = Menu(mymenu)

mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo")
newmenu.add_command(label="Redo")

root.mainloop()