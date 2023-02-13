import sqlite3
import tkinter as tk
from tkinter import messagebox
import NewUser



class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # widgets
        # Labels

        LoginLabel = tk.Label(self, text="Login", font=(12))
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.UserNameEntry = tk.Entry(self, width=30, textvariable=self.username)
        self.PasswordEntry = tk.Entry(self, width=30, textvariable=self.password)
        UserNameLabel = tk.Label(self, text="Username")
        PasswordLabel = tk.Label(self, text="Password")

        # Buttons
        LoginButton = tk.Button(self, text="Login", command=lambda: (self.login()))
        NewUserButton = tk.Button(self, text="Sign Up", command=lambda: controller.show_frame(NewUser.NewUserWindow))

        # Putting widgets on the screen
        LoginLabel.grid(row=0, column=1)
        PasswordLabel.grid(row=2, column=0)
        UserNameLabel.grid(row=1, column=0)
        self.UserNameEntry.grid(row=1, column=1)
        self.PasswordEntry.grid(row=2, column=1)
        LoginButton.grid(row=3, column=1)
        NewUserButton.grid(row=4, column=1)

    def login(self):
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()
        find_user = "SELECT * FROM Users WHERE username = ? and password = ?"
        c.execute(find_user, [(self.UserNameEntry.get()), (self.PasswordEntry.get())])

        result = c.fetchall()
        if result:
            tk.messagebox.showinfo("Success", "Logged in Successfully")
        else:
            tk.messagebox.showerror("Failed", "Invalid Credentials")

        conn.commit()
        conn.close()

