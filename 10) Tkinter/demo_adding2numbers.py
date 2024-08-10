from tkinter import *

root = Tk()
root.geometry("300x300")

def add():
    n1 = int(number1.get())
    n2 = int(number2.get())
    result = str(n1 + n2)
    answer.config(text="Anser is: "+ result)

number1  = Entry()
number2  = Entry()
number1.pack()
number2.pack()

button = Button(root,text='Add',command=add)
button.pack()

answer = Label(root)
answer.pack()

root.mainloop()