import tkinter as tk
import Revision

class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        test = tk.Label(self, text = "Login Screen")
        test.pack()
        Login_Button = tk.Button(self, text = "Login", command = lambda: controller.show_frame(Revision.TestWindow))
        Login_Button.pack()
