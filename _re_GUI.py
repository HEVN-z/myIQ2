############################################################################################
## Import packages
############################################################################################

from threading import Thread
from multiprocessing import Process
from tkinter import *
from tkinter import messagebox
import time

############################################################################################
## Import files
############################################################################################

import _re_Run as r
import _reJson_UID as J

print("\nLoading ... 1")

###############################################################################################
## Global Variables
###############################################################################################

App_still_running = True
Trade_real = False

###############################################################################################
## Function
###############################################################################################

def connect():
        if en_email.get() == "" or en_password.get() == "":
                messagebox.showerror("Login Fail", "Try again, Check your email or password")
                return
        J.set_email(en_email.get())
        J.set_password(en_password.get())
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
                thread_balance.start()
                go_frame2()
        except Exception as err:
                messagebox.showerror("Login Fail", "Try again, Check your email or password")
                print("Try again")
                print(err)
        #R.start()

def connect_thread():
        t1 = Thread(target=connect)
        t1.start()
        t1.join()

def getbalance():
        try:
                if r.bot.get_balance_mode() == 'REAL':
                        type = 'REAL'
                        color = 'green'
                elif r.bot.get_balance_mode() == 'PRACTICE':
                        type = 'PRACTICE'
                        color = 'orange'
                lb_balance.configure(text = type+" \n"+str(r.bot.get_balance())+" "+r.bot.get_currency(),
                                        fg = color)
        except Exception as err:
                print(err)
        print(r.bot.get_balance())
def getbalance_update():  
        while App_still_running:
                getbalance()    # update balance
                time.sleep(1)
def tradereal_toggle():
        global Trade_real
        Trade_real = not Trade_real
        if Trade_real:
                r.bot.change_balance('REAL')
                getbalance()
        else:
                r.bot.change_balance('PRACTICE')
                getbalance()
print("\nLoading ... 2")
def start():
        thread_running.start()

def stop():
        thread_running.stop()
print("\nLoading ... 3")

###############################################################################################
## Switch between frames
###############################################################################################

def go_frame2():
        frame2.tkraise()
        root.geometry("300x500")
def go_frame3():
        frame3.tkraise()
def on_closing():
        global App_still_running
        App_still_running = False
        r.App_still_running = False
        root.destroy()
###############################################################################################
## Thread
###############################################################################################

thread_running = Thread(target=r.run)
thread_balance = Thread(target=getbalance)

########################################################################################################################
## Create Widget's Class
########################################################################################################################

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

########################################################################################################################
## Create a TKinter window
########################################################################################################################

if __name__ == "__main__": 
        root = Tk()
        root.title("IQ Autobot")
        root.resizable(0,0)
        root.winfo_width()/2
        root.winfo_height()/2
        set_width = 250
        set_height = 250
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
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.protocol("WM_DELETE_WINDOW", on_closing)

############################################################################################
## Create the widgets
############################################################################################

        # Create frames

        frame1 = Frame(root)
        frame2 = Frame(root)
        frame3 = Frame(root)
        
        for frame in (frame1, frame2, frame3):
                frame.grid(row=0,column=0,sticky='nsew')

        ############################################################################################
        ## Frame 1
        # Create strings

        string_email = StringVar()
        string_email.set(J.get_email())
        string_password = StringVar()
        string_password.set(J.get_password())

        # Create widgets
        
        lb_email = Label(frame1, text="e-mail:")
        lb_email.pack(side=TOP, padx=10, pady=10)

        en_email = Entry(frame1, width=30, borderwidth=2,textvariable=string_email)
        print(J.get_email())
        en_email.pack(fill='x',padx=10, pady=10)

        lb_password = Label(frame1, text="Password:")
        lb_password.pack(side=TOP, padx=10, pady=10)

        en_password = Entry(frame1, width=30, show="*", borderwidth=2, textvariable=string_password)
        print(J.get_password())
        en_password.pack(fill='x',padx=10, pady=10)

        bt_start = Button(frame1, text = "Connect", command = connect)
        bt_start.pack(padx=10, pady=10)

        ############################################################################################
        ## Frame 2

        lb_balance = Label(frame2, text="Balance:",font=("Helvetica", 26))
        lb_balance.pack(side=TOP, padx=10, pady=10)

        bt_Stop = Button(frame2, text = "Balance Toggle", command = tradereal_toggle)
        bt_Stop.place(relx=.8, rely=.9, anchor=CENTER)

        ############################################################################################
        ## Frame 3

        print("\nLoading ... 4")
        frame1.tkraise()
        root.mainloop()
        print("\nLoading ... 5")

        ############################################################################################