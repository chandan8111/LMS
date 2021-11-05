from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
import dashboard   
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as mbx 

class mainWindow:
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
        self.win.title(" VIEW BOOK | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image = ImageTk.PhotoImage(Image.open("image\lmsl.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()




        self.but = Button(self.frame, text='GO TO Menu >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=125, y=480)

        self.but = Button(self.frame, text='Submit >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.addBook)
        self.but.place(x=625, y=480)

        self.mainloop()

    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()

    def addBook(self):
        pass