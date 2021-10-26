# First page of Library Management System..
from tkinter import *
from PIL import Image, ImageTk
import loginPage
import registerPage

class Welcome:
    # creating a constructor
    def __init__(self):
        self.win = Tk()
        # window background color using canvas
        self.canvas = Canvas(self.win, width=960, height=540, bg="white")
        self.canvas.pack(fill=BOTH, expand=YES)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        sp_width = int(width / 2 - 960 / 2)
        sp_height = int(height / 2 - 540 / 2)
        gem_size = "960x540+" + str(sp_width) + "+" + str(sp_height)
        self.win.geometry(gem_size)

        # disable resize window
        self.win.resizable(False, False)

        # Title of the window
        self.win.title("WELCOME | LIBRARY MANAGEMENT SYSTEM |")

    def add_content(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)
        # x, y = 70, 20

        self.image = ImageTk.PhotoImage(Image.open("image\lms.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        self.but = Button(self.frame, text='GO TO Register >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.registerPage)
        self.but.place(x=45, y=480)

        self.but = Button(self.frame, text='GO TO LOGIN >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.loginPage)
        self.but.place(x=720, y=480)

        self.win.mainloop()

    def loginPage(self):
        self.win.destroy()
        lobj = loginPage.loginWindow()
        lobj.add_content()

    def registerPage(self):
        self.win.destroy()
        robj = registerPage.loginWindow()
        robj.add_content()

if __name__ == "__main__":
    obj = Welcome()
    obj.add_content()