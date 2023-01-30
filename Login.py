import tkinter as tk

import NewUser
import Revision
import database_manager




class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


        #widgets
        #Labels

        LoginLabel = tk.Label(self, text = "Login", font = (12))

        UserNameEntry = tk.Entry(self, width = 30)
        PasswordEntry = tk.Entry(self, width = 30)
        UserNameLabel = tk.Label(self, text = "Username")
        PasswordLabel = tk.Label(self, text = "Password")

        #Buttons
        LoginButton = tk.Button(self, text = "Login", command = lambda: controller.show_frame(Revision.RevisionWindow))
        NewUserButton = tk.Button(self, text = "Sign Up", command = lambda :controller.show_frame(NewUser.NewUserWindow))



        #Putting widgets on the screen
        LoginLabel.grid(row = 0, column = 1)
        PasswordLabel.grid(row = 2, column = 0)
        UserNameLabel.grid(row =1, column = 0 )
        UserNameEntry.grid(row = 1, column = 1)
        PasswordEntry.grid(row = 2, column = 1)
        LoginButton.grid(row = 3, column=1)
        NewUserButton.grid(row = 4, column=1)
