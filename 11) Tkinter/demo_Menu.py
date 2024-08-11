from tkinter import *

root = Tk()
my_menu = Menu(root)
root.config(menu=my_menu)

submenu = Menu(my_menu)

my_menu.add_cascade(label='File',menu=submenu)

root.mainloop()