from tkinter import *

root = Tk()
root.geometry("300x300")

def selected():
    label.config(text=check_value.get())

check_value = BooleanVar()
checkbutton = Checkbutton(root,text="Accept terms",variable=check_value,command=selected)
checkbutton.pack()

label = Label(root)
label.pack()


root.mainloop()