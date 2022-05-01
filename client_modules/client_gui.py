import tkinter as tk

def p(pp):
    print(pp)

gui = tk.Tk()
gui.title("GUI")
gui.minsize(width=900, height=600)
gui.resizable(width=False, height=False)

bt_start = tk.Button(gui, text="Start", command=lambda: p("This is gui"))
bt_start.pack()