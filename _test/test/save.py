from tkinter import *
import os

if os.path.isfile('text.txt'):
    with open("text.txt", "r") as f:
        lineList = f.readlines()
        _, option1, _, option2 = lineList[-1].split()
else:
    option1 = '0'
    option2 = '0'

master = Tk()
master.minsize(200, 100)

var = IntVar()
var2 = IntVar()

a = Checkbutton(master, text="Option 1", variable=var)
if option1 == '1':
    a.select()
a.pack()

b = Checkbutton(master, text="Option 2", variable=var2)
if option2 == '1':
    b.select()
b.pack()

def save():
    text_file = open("text.txt", "a")
    text_file.write("Option1 %d Option2 %d \n" % (var.get(), var2.get()))
    text_file.close()

Button(master, text = "Save", command = save ).pack()

mainloop()