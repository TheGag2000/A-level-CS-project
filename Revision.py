import tkinter as tk
import Login

class RevisionWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        test = tk.Label(self, text = "test Window")
        test.pack()
        Test_Button = tk.Button(self, text = "Return to Login Screen", command = lambda: controller.show_frame(Login.LoginWindow))#Button to swithch between windows
        Test_Button.pack()
