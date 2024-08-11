from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

frame2 = Frame(root)
frame2.pack()

button = Button(frame,text="Button1")
button2 = Button(frame2,text="Button2")

button.pack()
button2.pack()

root.geometry("300x300")



root.mainloop()