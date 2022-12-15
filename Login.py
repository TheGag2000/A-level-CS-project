import tkinter as tk
import Revision
import sqlite3

class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #Connect to database
        conn = sqlite3.connect('Users.db')

        #Create cursor for database
        c = conn.cursor()
        #
        # #Create database
        # c.execute("""CREATE TABLE UserList (
        # user_name text,
        # password text
        #
        #
        # )
        #
        #
        #
        # """)



        #widgets
        LoginLabel = tk.Label(self, text = "Login")
        LoginLabel.grid(row = 0, column = 0)
        UserNameEntry = tk.Entry(self, width = 30)
        PasswordEntry = tk.Entry(self, width = 30)
        UserNameLabel = tk.Label(self, text = "Username")
        PasswordLabel = tk.Label(self, text = "Password")
        Login_Button = tk.Button(self, text = "Login", command = lambda: controller.show_frame(Revision.RevisionWindow))



        #Putting widgets on the screen
        PasswordLabel.grid(row = 2, column = 0)
        UserNameLabel.grid(row =1, column = 0 )
        UserNameEntry.grid(row = 1, column = 1)
        PasswordEntry.grid(row = 2, column = 1)
        Login_Button.grid(row=3, column=0, columnspan=2)

        #commiting database changes
        conn.commit()
