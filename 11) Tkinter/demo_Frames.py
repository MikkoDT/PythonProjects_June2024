from tkinter import *

root = Tk()

frame1 = Frame(root,highlightthickness=5,highlightbackground="Red",padx="20",pady="20")
frame1.pack()

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

button = Button(frame1,text="Button1")
button2 = Button(frame2,text="Button2")

button.pack()
button2.pack()

root.geometry("300x300")



root.mainloop()