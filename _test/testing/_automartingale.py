import tkinter as tk
import random
import _autojson as jsn
#import _automonitoring as mon

g = tk.Tk()
g.title("RANDOM")
g.minsize(width=200, height=300)
g.resizable(width=False, height=False)

def random_number():
    rand = random.randint(1, 3)
    if rand == 1:
        res = "LOSE"
        col = "red"
        jsn.set_amount(jsn.get_amount() - 1)
    elif rand == 2:
        res = "DRAW"
        col = "gray"
        jsn.set_amount(jsn.get_amount() + 0)
    else:
        res = "WIN"
        col = "green"
        jsn.set_amount(jsn.get_amount() + 1)
    lb_random.configure(text = res, foreground=col)
    lb_amount.configure(text = str(jsn.get_amount()))

def set_amount():
    try:
        jsn.set_amount(float(en_amount.get()))
        lb_amount.configure(text=jsn.get_amount())
    except:
        lb_amount.configure(text="Incorrect amount")

#def show_gui2():
#    mon.gui2.mainloop()
    
en_amount = tk.Entry(master=g, width=15)
en_amount.pack(pady=10)

bt_amount = tk.Button(master=g, width=15, height=1, text="Set Amount", command=set_amount)
bt_amount.pack()

bt_random = tk.Button(master = g, width=15, height=1, text="Random", command=random_number)
bt_random.pack()

lb_random = tk.Label(master = g, width=15, height=1, text = ' This is random ',background="white")
lb_random.pack()

lb_amount = tk.Label(master = g, width=15, height=1,text = str(jsn.get_amount()))
lb_amount.pack(pady=15)

#bt_monitoring = tk.Button(master = g, width=15, height=1, text="Monitoring", command=show_gui2)
#bt_monitoring.pack()

g.mainloop()
