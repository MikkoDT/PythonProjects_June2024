from tkinter import *

def function1():
    print("Menu item clicked.")

root = Tk()
my_menu = Menu(root)
root.config(menu=my_menu)

submenu = Menu(my_menu)

my_menu.add_cascade(label='File',menu=submenu)

submenu.add_command(label='Project',command=function1)
submenu.add_command(label='Save',command=function1)

status = Label(root,text="This is the current status.",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()