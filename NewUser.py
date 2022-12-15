import tkinter as tk
import Login

class NewUserWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #widgets
        #Labels

        SignUpLabel = tk.Label(self, text = "Sign Up", font=(12))
        SignUpLabel.grid(row = 0, column = 1)
        UserNameEntry = tk.Entry(self, width = 30)
        PasswordEntry = tk.Entry(self, width = 30)
        UserNameLabel = tk.Label(self, text = "Username")
        PasswordLabel = tk.Label(self, text = "Password")

        #Buttons
        ReturToLoginButton = tk.Button(self, text = "Return to Login Page", command = lambda: controller.show_frame(Login.LoginWindow))
        NewUserButton = tk.Button(self, text = "Create New Account")



        #Putting widgets on the screen
        PasswordLabel.grid(row = 2, column = 0)
        UserNameLabel.grid(row =1, column = 0 )
        UserNameEntry.grid(row = 1, column = 1)
        PasswordEntry.grid(row = 2, column = 1)
        ReturToLoginButton.grid(row = 4, column=0, columnspan = 2)

        NewUserButton.grid(row = 3, column=0, columnspan = 2)
