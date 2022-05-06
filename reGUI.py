import reRun as r
from threading import Thread
from tkinter import *

R = Thread(target=r.run)


def start():
        R.start()

def stop():
        R.raise_exception()
root = Tk()
root.title("IQ Autobot")
root.resizable(0,0)
root.winfo_width()/2
root.winfo_height()/2
set_width = 750
set_height = 350
w_center = set_width/2
h_center = set_height/2
x_center = root.winfo_screenwidth()/2
y_center = root.winfo_screenheight()/2
root.geometry("%dx%d+%d+%d" % (
        set_width,
        set_height,
        x_center-w_center,
        y_center-h_center))
root.attributes("-topmost", True)

bt_Stop = Button(root, text="Stop", command = stop)
bt_Stop.place(relx=0.7, rely=0.7, anchor=CENTER)

bt_start = Button(root, text="Start", command = start)
bt_start.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()