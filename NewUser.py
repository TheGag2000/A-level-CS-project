import tkinter as tk
import Login
import sqlite3
from tkinter import messagebox

class NewUserWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # widgets
        # Labels
        SignUpLabel = tk.Label(self, text="Sign Up", font=(12))
        SignUpLabel.grid(row=0, column=1)
        self.UserNameEntry = tk.Entry(self, width=30)
        self.PasswordEntry = tk.Entry(self, width=30)
        UserNameLabel = tk.Label(self, text="Username")
        PasswordLabel = tk.Label(self, text="Password")

        # Buttons
        ReturnToLoginButton = tk.Button(self, text="Return to Login Page",
                                        command=lambda: controller.show_frame(Login.LoginWindow))
        NewUserButton = tk.Button(self, text="Create New Account", command=lambda: self.add_user())

        # Putting widgets on the screen
        PasswordLabel.grid(row=2, column=0)
        UserNameLabel.grid(row=1, column=0)
        self.UserNameEntry.grid(row=1, column=1)
        self.PasswordEntry.grid(row=2, column=1)
        ReturnToLoginButton.grid(row=4, column=0, columnspan=2)

        NewUserButton.grid(row=3, column=0, columnspan=2)

    def add_user(self):
        conn = sqlite3.connect('Users.db')

        c = conn.cursor()
        c.execute("INSERT INTO Users VALUES (:username, :password)",  # Adds users details to database
                  {
                      'username': self.UserNameEntry.get(),
                      'password': self.PasswordEntry.get()
                  }
                  )
        conn.commit()
        conn.close()

        self.UserNameEntry.delete(0, tk.END)  # Clears the text boxes after submitting
        self.PasswordEntry.delete(0, tk.END)
        tk.messagebox.showinfo("New User created", "Your account has been created")# shows message box for user being created