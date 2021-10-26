from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import loginPage

class dashBoard:
    def __init__(self):
        self.win = Tk()

        # window background color using canvas
        self.canvas = Canvas(self.win, width=960, height=670, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 960 / 2)
        y = int(height / 2 - 670 / 2)
        str1 = "960x670+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(False, False)

        # changing title of the window
        self.win.title("| DASHBOARD | LIBRARY MANAGEMENT SYSTEM |")
    
    def add_menu(self):
        self.frame = Frame(self.win, height=670, width=960)
        self.frame.place(x=0, y=0)

        self.image = ImageTk.PhotoImage(Image.open("image\lmsd.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        # welcome text
        self.label = Label(self.frame, text=" WELCOME TO LIBRARY MANAGEMENT SYSTEM")
        self.label.config(font=("Courier", 20, 'underline bold'))
        self.label.place(x=170, y=20)

        # Detail button and logout
        self.label = Label(self.frame, text="Chandan")
        self.label.config(font=("Courier", 20))
        self.label.place(x=55, y=90)

        self.but = Button(self.frame, text='Detail', width=15, bg='light grey', fg='black',
                          font=("Poppins", 13, " bold"))
        self.but.place(x=450, y=90)

        self.but = Button(self.frame, text='Log Out', width=15, bg='light grey', fg='black',
                          font=("Poppins", 13, " bold"), command=self.logOut)
        self.but.place(x=750, y=90)

        # About student Button
        self.label = Label(self.frame, text=" STUDENT ")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=55, y=160)
        # Student row 1
        self.but = Button(self.frame, text='Add Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=55, y=230)

        self.but = Button(self.frame, text='Update Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=355, y=230)

        self.but = Button(self.frame, text='Delete Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=655, y=230)
        # Student row 2
        self.but = Button(self.frame, text='View Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=55, y=300)

        self.but = Button(self.frame, text='Search Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=355, y=300)

        self.but = Button(self.frame, text='Book Leaded By Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=655, y=300)
        
        self.label = Label(self.frame, text="BOOKS")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=55, y=370)
        # Row 1
        self.but = Button(self.frame, text='ADD BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=55, y=440)

        self.but = Button(self.frame, text='EDIT BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=355, y=440)

        self.but = Button(self.frame, text='DELETE BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=655, y=440)

        # Row 2
        self.but = Button(self.frame, text='BOOK LEADING', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=55, y=510)

        self.but = Button(self.frame, text='RETURN BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=355, y=510)

        self.but = Button(self.frame, text='VIEW BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=655, y=510)

        # row 3
        self.but = Button(self.frame, text='SEARCH BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=55, y=580)

        self.but = Button(self.frame, text='REPORT', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=355, y=580)

        self.but = Button(self.frame, text='ABOUT', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"))
        self.but.place(x=655, y=580)

    def add_frame(self):
        
        self.win.mainloop()

    def logOut(self):
        self.mess = messagebox.askquestion('LogOut Account','Are you sure you want to logout the account',icon = 'warning')
        if self.mess == 'yes':
            self.win.destroy()
            lobj = loginPage.loginWindow()
            lobj.add_content()
        else:
            pass


if __name__ == "__main__":
    dh = dashBoard()
    dh.add_menu()
    dh.add_frame()