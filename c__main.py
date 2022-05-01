from c_gui import gui as g, bt_start


bt_start.configure(command=lambda: print("This is main"))

g.mainloop()