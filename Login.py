import tkinter as tk
class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        test = tk.Label(self, text = "test Window")
        test.pack()
