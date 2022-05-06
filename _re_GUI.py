############################################################################################
## Import packages
############################################################################################

from threading import Thread
from tkinter import *

############################################################################################
## Import files
############################################################################################

import _re_Run as r
import _reJson_UID as J

print("\nLoading ... 1")

###############################################################################################
## Global Variables
###############################################################################################

R = Thread(target=r.run)

###############################################################################################
## Function
###############################################################################################

def connect():
        r.refresh_login()
        if r.bot.check_connect():
                print("Connected")
        else:
                print("Try again")
        try:
                print(r.bot.get_balance())
                print(r.bot.get_balance_mode())
                r.bot.change_balance('REAL')
                print(r.bot.get_balance())
                print(r.bot.get_balance_mode())
                r.bot.change_balance('PRACTICE')
                print(r.bot.get_balance())
                print(r.bot.get_balance_mode())
        except Exception as err:
                print("Try again")
                print(err)
        R.start()

def connect_thread():
        t1 = Thread(target=connect)
        t1.start()
        t1.join()

def getballance():
        print(r.bot.get_balance())

print("\nLoading ... 2")
def start():
        R.start()

def stop():
        R.stop()
print("\nLoading ... 3")

########################################################################################################################
## Create a TKinter window
########################################################################################################################

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


############################################################################################
## Create the widgets
############################################################################################


# Create frames

frame1 = Frame(root, bg="white")
frame1.pack(fill=BOTH, expand=1)


# Create buttons

bt_Stop = Button(frame1, text="Show Balance", command = getballance)
bt_Stop.place(relx=0.7, rely=0.7, anchor=CENTER)

bt_start = Button(frame1, text="Connect", command = connect)
bt_start.place(relx=0.5, rely=0.5, anchor=CENTER)

print("\nLoading ... 4")

root.mainloop()