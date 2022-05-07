############################################################################################
## Import packages
############################################################################################

from math import floor
from threading import Thread
from tkinter import *
from tkinter import messagebox
import time

############################################################################################
## Import files
############################################################################################

import _re_Run as r
import JSON._reJson_UID as J

print("\nLoading ... 1")

###############################################################################################
## Global Variables
###############################################################################################

App_still_running = True
Trade_real = False
isFullscreen = False

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
                #print(r.bot.get_balance_mode())
                #r.bot.change_balance('REAL')
                #print(r.bot.get_balance())
                #print(r.bot.get_balance_mode())
                #r.bot.change_balance('PRACTICE')
                #print(r.bot.get_balance())
                #print(r.bot.get_balance_mode())
                thread_balance.start()
                go_frame2()
                J.set_email_remember(en_email.get())
                J.set_password_remember(en_password.get())
        except Exception as err:
                messagebox.showerror("Login Fail", "Try again, Check your email or password")
                print("Try again")
                print(err)
        #R.start()

def connect_thread():
        t1 = Thread(target=connect)
        t1.start()
        t1.join()

###############################################################################################
## Function balance
###############################################################################################

def formal_number(number):
        floor_number = floor(number)
        floor_number = str(floor_number)
        if len(floor_number) > 6:
                floor_number = floor_number[:-6] + "," + floor_number[-6:]
        if len(floor_number) > 3:
                floor_number = floor_number[:-3] + "," + floor_number[-3:]
        remain_number = round(number%1,2)
        if remain_number != 0:
                remain_number = str(remain_number)
                remain_number = remain_number[1:]
                floor_number += remain_number
        return floor_number
def getbalance():
        try:
                if r.bot.get_balance_mode() == 'REAL':
                        type = 'REAL'
                        color = 'lime'
                        ccolor = '#2ECC71'
                elif r.bot.get_balance_mode() == 'PRACTICE':
                        type = 'DEMO'
                        color = 'yellow'
                        ccolor = 'orange'
                balance = r.bot.get_balance()
                lb_currency.config(text=type+"\n"+r.bot.get_currency(),fg= ccolor)
                lb_balance.configure(text =formal_number(balance),fg = color)
                en_amount.configure(bg = color,disabledforeground=color)
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
        #root.minsize(300,500)
        root.geometry("300x500"+"+{}+{}".format(root.winfo_screenwidth()//2-150,root.winfo_screenheight()//2-250))
        #root.resizable(1,1)
def frame2_go_fullscreen():
        global isFullscreen
        if isFullscreen:
                root.attributes("-fullscreen", False)
                emptyMenu = Menu(root)
                root.config(menu=emptyMenu)
                bt_toggle_fullscreen.configure(text="Full View")
                lb_debugging_text.configure(text=str(root.winfo_width())+"x"+str(root.winfo_height()))
        else:
                root.attributes("-fullscreen", True)
                root.config(menu=frame2_menubar)
                bt_toggle_fullscreen.configure(text="Compact View")
                lb_debugging_text.configure(text=str(root.winfo_width())+"x"+str(root.winfo_height()))
        isFullscreen = not isFullscreen
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

###############################################################################################
## UI config
###############################################################################################

def auto_trade_enable():
        if J.get_auto_trade_enable() == 0:
                J.set_auto_trade_enable(1)
                bt_manual_buy['state'] = 'disabled'
                bt_manual_sell['state'] = 'disabled'
                print("Auto trade enabled")

        elif J.get_auto_trade_enable() == 1:
                J.set_auto_trade_enable(0)
                bt_manual_buy['state'] = 'normal'
                bt_manual_sell['state'] = 'normal'
                print("Auto trade disabled")
        else:
                print("Error")

def auto_trade_enable_update():
        if J.get_auto_trade_enable() == 1:
                bt_manual_buy['state'] = 'disabled'
                bt_manual_sell['state'] = 'disabled'
        elif J.get_auto_trade_enable() == 0:
                bt_manual_buy['state'] = 'normal'
                bt_manual_sell['state'] = 'normal'
        else:
                print("Error")

def auto_mm_enable():
        if J.get_auto_mm_enable() == 0:
                J.set_auto_mm_enable(1)
                en_amount['state'] = 'disabled'
                print("Auto money management enabled")

        elif J.get_auto_mm_enable() == 1:
                J.set_auto_mm_enable(0)
                en_amount['state'] = 'normal'
                print("Auto money management disabled")
        else:
                print("Error")

def auto_mm_enable_update():
        if J.get_auto_mm_enable() == 1:
                en_amount['state'] = 'disabled'
        elif J.get_auto_mm_enable() == 0:
                en_amount['state'] = 'normal'
        else:
                print("Error")
########################################################################################################################
## Create popup windows
########################################################################################################################



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
        set_height = 180
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

        frame1 = Frame(root, bg='gray')
        frame2 = Frame(root, bg='gray')
        frame3 = Frame(root)
        
        for frame in (frame1, frame2, frame3):
                frame.grid(row=0,column=0,sticky='nsew')

        ############################################################################################
        ## Frame 1
        # Create Variables

        string_email = StringVar()
        string_email.set(J.get_email_remember())
        string_password = StringVar()
        string_password.set(J.get_password_remember())

        # Groupbox

        groupbox_login = LabelFrame(frame1, text="Login IQ Autobot", bg='gray')
        groupbox_login.pack(fill="both", expand="yes")

        # Create widgets
        
        lb_email = Label(groupbox_login,bg='gray', text="User email :",font=("Helvetica", 14))
        lb_email.place(relx=.1,rely=.1,anchor=W)

        en_email = Entry(groupbox_login,bg='#ABB2B9', width=30, borderwidth=2,textvariable=string_email)
        print(J.get_email_remember())
        en_email.place(relx=.5,rely=.25,anchor=CENTER)

        lb_password = Label(groupbox_login,bg='gray', text="Password :",font=("Helvetica", 14))
        lb_password.place(relx=.1,rely=.45,anchor=W)

        en_password = Entry(groupbox_login,bg='#ABB2B9', width=30, show="*", borderwidth=2, textvariable=string_password)
        print(J.get_password_remember())
        en_password.place(relx=.5,rely=.6,anchor=CENTER)

        bt_login = Button(groupbox_login,bg='#ABB2B9', text = "Connect", command = connect,width=10)
        bt_login.place(relx=.5,rely=.8,anchor=CENTER)

        ############################################################################################
        ## Frame 2
        # Create Variables

        ##
        ## CB Variables

        cb_auto_trade_enable_Var = IntVar()
        cb_auto_trade_enable_Var.set(J.get_auto_trade_enable())
        print("cb trade var = ", cb_auto_trade_enable_Var.get())
        cb_auto_mm_enable_Var = IntVar()
        cb_auto_mm_enable_Var.set(J.get_auto_mm_enable())
        print("cb trade var = ", cb_auto_mm_enable_Var.get())

        ## Frame 2 Menues

        frame2_menubar = Menu(root)
        #root.config(menu=frame2_menubar)

        frame2_submenu = Menu(frame2_menubar, tearoff=0)
        frame2_menubar.add_cascade(label="File", menu=frame2_submenu)
        frame2_submenu.add_command(label="New", command=root.destroy)
        frame2_submenu.add_command(label="Open", command=root.destroy)
        frame2_submenu.add_command(label="Save", command=root.destroy)
        frame2_submenu.add_separator()
        frame2_submenu.add_command(label="Exit", command=root.quit)
        

        helpmenu = Menu(frame2_menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=root.destroy)
        helpmenu.add_command(label="About...", command=lambda:messagebox.showinfo("About", "IQ Autobot.\n\nIQ Autobot is robot trading from IQOption broker\n\n\tBeta version 0.001b"))
        frame2_menubar.add_cascade(label="Help", menu=helpmenu)


        ## Frame 2 subframes

        frame2_balance = Frame(frame2, bg='black', width=285, height=60)
        frame2_balance.place(x=-8,relx=1, y=5, anchor=NE)

        frame2_uid = Frame(frame2, bg='#2E4053', width=185, height=28)
        frame2_uid.place(x=-108,relx=1, y=70, anchor=NE)

        frame2_today_profit = Frame(frame2, bg='red', width=185, height=28)
        frame2_today_profit.place(x=-108,relx=1, y=100, anchor=NE)

        frame2_trading_area = LabelFrame(frame2,text="Trading area", bg='gray', width=285, height=180)
        frame2_trading_area.place(x=-8,relx=1, y=130, anchor=NE)

        frame2_mm_area = LabelFrame(frame2,text="Money management area", bg='gray', width=285, height=180)
        frame2_mm_area.place(x=-8,relx=1, y=310, anchor=NE)

        ## Framw 2 widgets

        lb_currency = Label(frame2_balance,bg='black', text="Balance:",font=("Arial", 14,'bold'))
        lb_currency.place(relx=.15,rely=.5,anchor=CENTER)

        lb_balance = Label(frame2_balance,bg='black',font=("Arial 26 bold"),height=2)
        lb_balance.place(relx=1,rely=.5,anchor=E)

        lb_uid = Label(frame2,bg='#2E4053', text="UID : "+J.get_email()[:6]+"******", fg='#3498DB',font=("Arial", 14,'bold'))
        lb_uid.place(x=-290,relx=1, y=70, anchor=NW)

        bt_toggle_balance = Button(frame2,bg='#ABB2B9',width=12, text = "Balance Toggle", command = tradereal_toggle)
        bt_toggle_balance.place(x=-8,y=70,relx=1, anchor=NE)

        bt_toggle_fullscreen = Button(frame2,bg='#ABB2B9',width=12, text = "Full View", command = frame2_go_fullscreen)
        bt_toggle_fullscreen.place(x=-8,y=100,relx=1, anchor=NE)

        lb_debugging_text = Label(frame2,bg='#2E4053', text="Debugging text", fg='#3498DB',font=("Arial", 14,'bold'))
        lb_debugging_text.place(relx=1,rely=1,x=-5, y=-5, anchor=SE)

        ###############
        ## Trading Area
        bt_image_higher = PhotoImage(file = "images/higher.png").subsample(1,1)
        bt_image_lower = PhotoImage(file = "images/lower.png").subsample(1,1)
        bt_image_dim = 60
        bt_manual_buy = Button(frame2_trading_area,bg='lime', text = "Buy", command = 'manual_buy',
        width=bt_image_dim,height=bt_image_dim, image=bt_image_higher,
        font=("Helvetica", 18))
        bt_manual_buy.place(x=5,y=5,relx=0,rely=0,anchor=NW)

        bt_manual_sell = Button(frame2_trading_area,bg='red', text = "Sell", command = 'manual_sell',
        width=bt_image_dim,height=bt_image_dim, image=bt_image_lower,
        font=("Helvetica", 18))
        bt_manual_sell.place(x=5,y=-5,relx=0,rely=1,anchor=SW)

        cb_auto_trade_enable = Checkbutton(frame2_trading_area,bg='gray', text = "Auto Trade", command = auto_trade_enable,
        variable = cb_auto_trade_enable_Var,
        onvalue=1, offvalue=0,activebackground='gray',
        width=15)
        cb_auto_trade_enable.place(x=-20,y=5,relx=1,rely=0,anchor=NE)
        auto_trade_enable_update()
        if J.get_auto_trade_enable() == 1:
                cb_auto_trade_enable.select()
        
        bt_auto_trade_config = Button(frame2_trading_area,bg='gray', text = "..", command = "auto_trade_config")
        bt_auto_trade_config.place(x=-5,y=5,relx=1,rely=0,anchor=NE)

        ###############
        ## Money management area

        en_amount = Entry(frame2_mm_area, width=9, font=("Arial", 18,'bold'),
        disabledbackground='black')
        en_amount.place(x=5,y=5,relx=0,rely=0,anchor=NW)

        cb_auto_mm_enable = Checkbutton(frame2_mm_area,bg='gray', text = "Auto MM", command = auto_mm_enable,
        onvalue=1, offvalue=0,activebackground='gray',
        width=15,
        variable = cb_auto_mm_enable_Var)
        cb_auto_mm_enable.place(x=-20,y=5,relx=1,rely=0,anchor=NE)
        auto_mm_enable_update()
        if cb_auto_mm_enable_Var.get() == 1:
                cb_auto_mm_enable.select()
        
        bt_auto_mm_config = Button(frame2_mm_area,bg='gray', text = "..", command = "auto_mm_config")
        bt_auto_mm_config.place(x=-5,y=5,relx=1,rely=0,anchor=NE)

        ############################################################################################
        ## Frame 3
        
        print("\nLoading ... 4")
        frame1.tkraise()

        root.bind_all("<Button-1>", lambda event: event.widget.focus_set())
        root.mainloop()
        print("\nLoading ... 5")

        ############################################################################################