from tkinter import *
import tkinter as tk
import dashboard   
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as mbx 
from store import config
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
        self.win.title(" EDIT BOOK | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image = ImageTk.PhotoImage(Image.open("image\lmsdb.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()


        self.label = Label(self.frame, text="EDITING BOOKS", fg='black')
        self.label.config(font=("helvetica", 20))
        self.label.place(x=350, y=10)

        # Id
        self.label1 = Label(self.frame, text="BOOK ID")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=250, y=100)

        self.bid = Entry(self.frame, font="Arial 15")
        self.bid.place(x=450, y=100)

        self.butt1 = Button(self.frame, text='Check', width=6, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.check)
        self.butt1.place(x=700, y=100)


        # creating book title label and entry field
        self.label2 = Label(self.frame, text="BOOK NAME")
        self.label2.config(font=("Times", 15, 'bold'))
        self.label2.place(x=250, y=150)

        self.bkt = Entry(self.frame, font="Arial 15")
        self.bkt.place(x=450, y=150)

         # creating author name label and entry field
        self.label3 = Label(self.frame, text="AUTHOR NAME")
        self.label3.config(font=("Times", 15, 'bold'))
        self.label3.place(x=250, y=200)

        self.aut = Entry(self.frame, font="Arial 15")
        self.aut.place(x=450, y=200)

        # creating published year label and entry field
        self.label4 = Label(self.frame, text="PUBLISHED YEAR")
        self.label4.config(font=("Times", 15, 'bold'))
        self.label4.place(x=250, y=250)

        self.pub = Entry(self.frame, font="Arial 15")
        self.pub.place(x=450, y=250)

         # creating Book price label and entry field
        self.label5 = Label(self.frame, text="TOTAL PAGES")
        self.label5.config(font=("Times", 15, 'bold'))
        self.label5.place(x=250, y=300)

        self.page = Entry(self.frame, font="Arial 15")
        self.page.place(x=450, y=300)

        # creating Book category label and entry field
        self.label6 = Label(self.frame, text="BOOK CATEGORY")
        self.label6.config(font=("Times", 15, 'bold'))
        self.label6.place(x=250, y=350)

        self.cat = Entry(self.frame, font="Arial 15")
        self.cat.place(x=450, y=350)












        self.but = Button(self.frame, text='GO TO Menu >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=150, y=430)

        self.but = Button(self.frame, text=' ADD BOOK ', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.editBook)
        self.but.place(x=600, y=430)

        self.win.mainloop()
    

    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()

    def check(self):
        bookid= self.bid.get()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(f"SELECT title,author,publishedYear,totalPage,category FROM book where id={bookid}")
            mydata=cursor.fetchall()
            self.bkt.delete(0, END)
            self.bkt.insert(0, mydata[0][0])

            self.aut.delete(0, END)
            self.aut.insert(0, mydata[0][1])

            self.pub.delete(0, END)
            self.pub.insert(0, mydata[0][2])

            self.page.delete(0, END)
            self.page.insert(0, mydata[0][3])

            self.cat.delete(0, END)
            self.cat.insert(0, mydata[0][4])

            conn.close()

        except Error:
            mbx.showwarning("Error","Data not found.")
        
    def editBook(self):
        data=(
            self.bkt.get(),
            self.aut.get(),
            self.pub.get(),
            self.page.get(),
            self.cat.get()
        )
        bookid= self.bid.get()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            # cursor.execute(f"UPDATE book SET title={data[0]},author={data[1]},publishedYear={data[2]},totalPage={data[3]},category={data[4]}  WHERE id={booid}")
            cursor.execute("UPDATE book SET title=%s,author=%s,publishedYear=%s,totalPage=%s,category=%s  WHERE id=%s",(data[0],data[1],data[2],data[3],data[4],bookid))
            conn.commit()
            conn.close()
            mbx.showinfo("Sucessfull","Your book data has been uploaded.")

        except Error:
            mbx.showwarning("Server Error","Can not connect to \ndatabase and upload data")