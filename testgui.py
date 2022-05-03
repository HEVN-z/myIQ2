from tkinter import *

def set_lb():
    i = int(w.get())
    if i > 10:
        i = 10
    elif i < 0:
        i = 0
    lb.configure(text = i)



master = Tk()
master.title("IQOption_Autobot")
#master.state('zoomed')
master.resizable(0,0)
master.geometry("400x400")
#master.attributes("-topmost", True)
master.attributes("-fullscreen", True)
t_checker = False

def new_win():
    def close():
        global t_checker
        t_checker = False
        t.destroy()
    global t_checker
    if t_checker:
        return
    t_checker = True
    t = Toplevel(master)
    t.wm_resizable(width=False, height=False)
    t.title("New window")
    t.transient(master)
    t.focus()
    t.protocol("WM_DELETE_WINDOW", lambda: close())

w = Spinbox(master, from_=0, to=10)
w.pack()

bt = Button(master, text="OK", command=new_win)
bt.pack()

lb = Label(master, text="This is label")
lb.pack()

bt_close = Button(master, text="Close", command=master.destroy)
bt_close.pack()

mainloop()