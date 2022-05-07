import tkinter as tk
from tkinter import ttk
from turtle import bgcolor

# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

root.grid()

#
style = ttk.Style()
style.theme_use('clam')
#style.configure('TProgressbar', background='blue', foreground='red')

#style2 = ttk.Style()
#style2.theme_use('clam')
#style2.configure('Horizontal.TProgressbar', background='violet', foreground='red')
# progressbar
pb = ttk.Progressbar(
    root,
    value=90,
    orient='horizontal',
    mode='determinate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# start button
start_button = ttk.Button(
    root,
    text='Start',
    command=lambda:pb.configure(value=50)#pb.start
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
    root,
    text='Stop',
    command=pb.stop
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


root.mainloop()