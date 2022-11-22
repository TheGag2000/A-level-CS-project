import tkinter as tk #imports the tkinter library to bo be used to create GUI

#RevisionApp class is used to configure application to allow for OOP windows

class LoginWindow(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self,parent)
        test = tk.Label(self, text = "test Window")
        test.pack()

class RevisionApp(tk.Tk): #RevisionApp class inherits from tk.Tk
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #initialises tkinter to be used within the revisionap class
        container = tk.Frame(self) # container used to contain all the elements of the app
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = LoginWindow(container, self)

        self.frames[LoginWindow] = frame
        frame.grid(row=0, column = 0, sticky = "nsew")

        self.show_frame(LoginWindow)

    def show_frame(self, cont): #shows the selected window in the frame
        frame = self.frames[cont]
        frame.tkraise()



app = RevisionApp()
app.mainloop()

