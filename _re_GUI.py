import _re_Run as r
from threading import Thread
from tkinter import *

def p(text):
        print(text)
p("\nLoading ... 1")
bot = r.bot = r.IQ_Option(r.email,r.password)
def connect():
        bot.connect()
        try:
                bot.get_balance()
                p("Connected")
        except:
                p("Try again")
C = Thread(target=connect)
R = Thread(target=r.run)


def getballance():
        p(bot.get_balance())

p("\nLoading ... 2")
def start():
        R.start()

def stop():
        R.stop()
p("\nLoading ... 3")
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

bt_Stop = Button(root, text="Stop", command = getballance)
bt_Stop.place(relx=0.7, rely=0.7, anchor=CENTER)

bt_start = Button(root, text="Connect", command = connect)
bt_start.place(relx=0.5, rely=0.5, anchor=CENTER)
p("\nLoading ... 4")
root.mainloop()