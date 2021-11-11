from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import loginPage
import student.addStudent
import student.updateStudent
import student.viewStudent
import student.searchStudent
import student.deleteStudent
import book.addBook
import book.editBook
import book.searchBook
import book.bookLeading
import book.returnBook




def leadedByStudent():
    pass


def about():
    pass


class dashBoard:
    def __init__(self):
        self.win = Tk()

        # window background color using canvas
        self.canvas = Canvas(self.win, width=960, height=600, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 960 / 2)
        y = int(height / 2 - 600 / 2)
        str1 = "960x600+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        self.win.resizable(False, False)

        # changing title of the window
        self.win.title("| DASHBOARD | LIBRARY MANAGEMENT SYSTEM |")
    
    def add_menu(self):
        self.frame = Frame(self.win, height=600, width=960)
        self.frame.place(x=0, y=0)

        self.image = ImageTk.PhotoImage(Image.open("image\lmsd.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        # welcome text
        self.label = Label(self.frame, text=" WELCOME TO LIBRARY MANAGEMENT SYSTEM")
        self.label.config(font=("Courier", 20, 'underline bold'))
        self.label.place(x=170, y=20)

        #  logout


        self.but = Button(self.frame, text='Log Out', width=15, bg='light grey', fg='black',
                          font=("Poppins", 13, " bold"), command=self.logOut)
        self.but.place(x=750, y=90)

        # About student Button
        self.label = Label(self.frame, text=" STUDENT ")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=55, y=160)
        # Student row 1
        self.but0 = Button(self.frame, text='Add Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.addStudent)
        self.but0.place(x=55, y=230)

        self.but1 = Button(self.frame, text='Update Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.updateStudent)
        self.but1.place(x=355, y=230)

        self.but = Button(self.frame, text='Delete Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.deleteStudent)
        self.but.place(x=655, y=230)
        # Student row 2
        self.but = Button(self.frame, text='View Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.viewStudent)
        self.but.place(x=55, y=300)

        self.but = Button(self.frame, text='Search Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.searchStudent)
        self.but.place(x=355, y=300)

        self.but = Button(self.frame, text='Book Leaded By Student', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=leadedByStudent)
        self.but.place(x=655, y=300)
        
        self.label = Label(self.frame, text="BOOKS")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=55, y=370)
        # Row 1
        self.but = Button(self.frame, text='ADD BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.addBook)
        self.but.place(x=55, y=440)

        self.but = Button(self.frame, text='EDIT BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.editBook)
        self.but.place(x=355, y=440)

        self.but = Button(self.frame, text='SEARCH AND DELETE', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.sedelBook)
        self.but.place(x=655, y=440)

        # Row 2
        self.but = Button(self.frame, text='BOOK LEADING', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command= self.bookLeading)
        self.but.place(x=55, y=510)

        self.but = Button(self.frame, text='RETURN BOOK', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=self.returnBook)
        self.but.place(x=355, y=510)

        self.but = Button(self.frame, text='ABOUT', width=20, bg='light grey', fg='black',
                          font=("Poppins", 15, " bold"), command=about)
        self.but.place(x=655, y=510)


        self.win.mainloop()

    def returnBook(self):
        self.win.destroy()
        obj=book.returnBook.mainWindow()
        obj.addframe()

    def bookLeading(self):
        self.win.destroy()
        obj=book.bookLeading.mainWindow()
        obj.addframe()

    def sedelBook(self):
        self.win.destroy()
        obj=book.searchBook.mainWindow()
        obj.addframe()
 
    def editBook(self):
        self.win.destroy()
        obj=book.editBook.mainWindow()
        obj.addframe()

    def addBook(self):
        self.win.destroy()
        obj=book.addBook.mainWindow()
        obj.addframe()
        
    def addStudent(self):
        self.win.destroy()
        obj1=student.addStudent.studentWindow()
        obj1.addframe()
    def updateStudent(self):
        self.win.destroy()
        obj2=student.updateStudent.studentWindow()
        obj2.addframe()
    def viewStudent(self):
        self.win.destroy()
        obj=student.viewStudent.studentWindow()
        obj.addframe()
    def searchStudent(self):
        self.win.destroy()
        obj=student.searchStudent.studentWindow()
        obj.addframe()
    def deleteStudent(self):
        self.win.destroy()
        obj=student.deleteStudent.studentWindow()
        obj.addframe()




    def logOut(self):
        self.mess = messagebox.askquestion('LogOut Account','Are you sure you want to logout the account',icon = 'warning')
        if self.mess == 'yes':
            self.win.destroy()
            lobj = loginPage.loginWindow()
            lobj.add_content()


if __name__ == "__main__":
    dh = dashBoard()
    dh.add_menu()