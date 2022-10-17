import tkinter as tk
from tkinter import *

class Window:
    def __init__(self, master):
        self.master = master
        self.geometry = master.geometry("1000x500")
        self.frame = tk.LabelFrame(self.master, text = "this is a frame",bg = "white")

        self.Label1 = tk.Label(self.frame, text = "test")
        self.Label1.pack()
        self.frame.pack()
