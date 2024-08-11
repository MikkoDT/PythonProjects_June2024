from tkinter import *

root = Tk()
root.geometry("300x300")
radio1 = Radiobutton(root,text="Petrol")
radio2 = Radiobutton(root,text="Diesel")
radio3 = Radiobutton(root,text="Electric")

radio1.pack()
radio2.pack()
radio3.pack()

root.mainloop()