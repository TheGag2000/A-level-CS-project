import tkinter as tk
import NewUser
import Revision
import sqlite3

class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


        #widgets
        #Labels

        LoginLabel = tk.Label(self, text = "Login", font = (12))

        self.UserNameEntry = tk.Entry(self, width = 30)
        self.PasswordEntry = tk.Entry(self, width = 30)
        UserNameLabel = tk.Label(self, text = "Username")
        PasswordLabel = tk.Label(self, text = "Password")

        #Buttons
        LoginButton = tk.Button(self, text = "Login", command = lambda: controller.show_frame(Revision.RevisionWindow))
        NewUserButton = tk.Button(self, text = "Sign Up", command = lambda :controller.show_frame(NewUser.NewUserWindow))



        #Putting widgets on the screen
        LoginLabel.grid(row = 0, column = 1)
        PasswordLabel.grid(row = 2, column = 0)
        UserNameLabel.grid(row =1, column = 0 )
        self.UserNameEntry.grid(row = 1, column = 1)
        self.PasswordEntry.grid(row = 2, column = 1)
        LoginButton.grid(row = 3, column=1)
        NewUserButton.grid(row = 4, column=1)

    def login(self):
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()


        conn.commit()
        conn.close()

