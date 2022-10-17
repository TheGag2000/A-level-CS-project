
from Window import *
#importing window module responsible for creating windows




#runs the main script
if __name__ == '__main__':
    root = tk.Tk() #creates the root object for tkinter
    app = Window(root)#instatitates a test window
    root.mainloop()
