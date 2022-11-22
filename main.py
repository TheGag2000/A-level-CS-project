import tkinter as tk #imports the tkinter library to bo be used to create GUI
from Login import LoginWindow # imports the login window
from RevisionWindow import TestWindow


#RevisionApp class is used to configure application to allow for OOP windows
class RevisionApp(tk.Tk): #RevisionApp class inherits from tk.Tk
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #initialises tkinter to be used within the revisionap class
        container = tk.Frame(self) # container used to contain all the elements of the app
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (LoginWindow, TestWindow):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky = "nsew")

        self.show_frame(LoginWindow)

    def show_frame(self, cont): #shows the selected window in the frame
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = RevisionApp()
    app.mainloop()

