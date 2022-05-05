from tkinter import *

master = Tk()
master.title("IQOption_Autobot")
master.minsize(width=400, height=400)
display_width = master.winfo_screenwidth()
display_height = master.winfo_screenheight()
master.geometry("400x400+1000+50")
master.resizable(0,0)
master.attributes("-topmost", True)
#master.overrideredirect(True)
#master.attributes("-fullscreen", True)

Frame_1 = Frame(master, width=400, height=400)
Frame_1.pack(fill="both")



lb_main = Label(Frame_1, text = "windows size = " + str(display_width) + " x " + str(display_height), font=("Arial", 16))
lb_main.place(x=100, y=15)

#bt_exit = Button(Frame_1, text = "Exit" , command = master.destroy,width=15)
#bt_exit.place(x = 280, y=370)

master.mainloop()