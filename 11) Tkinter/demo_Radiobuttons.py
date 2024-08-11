from tkinter import *

root = Tk()
root.geometry("300x300")

fuel = StringVar(value="Petrol")

radio1 = Radiobutton(root,text="Petrol",variable=fuel,value="Petrol")
radio2 = Radiobutton(root,text="Diesel",variable=fuel,value="Diesel")
radio3 = Radiobutton(root,text="Electric",variable=fuel,value="Electric")

radio1.pack()
radio2.pack()
radio3.pack()

root.mainloop()