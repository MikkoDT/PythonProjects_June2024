from tkinter import *

def display():
    print('Button clicked')

root = Tk()
root.geometry("300x300")
button = Button(root,text="Click here",command=display)
button.pack()




root.mainloop()