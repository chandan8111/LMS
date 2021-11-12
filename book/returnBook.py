from tkinter import *
import tkinter as tk
import dashboard   
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as mbx 
from datetime import date
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
        self.win.title(" RETURN LENDING BOOKS | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image = ImageTk.PhotoImage(Image.open("image\lmsdb.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()


        self.label = Label(self.frame, text="RETURN BOOKS", fg='black')
        self.label.config(font=("helvetica", 20))
        self.label.place(x=350, y=10)

        # LEADING 
        self.label1 = Label(self.frame, text="LENDING ID :")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=150, y=125)

        self.sid = Entry(self.frame, font="Arial 15")
        self.sid.place(x=350, y=125)
        
        self.but = Button(self.frame, text=' GET DATA  ', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.leadid)
        self.but.place(x=350, y=175)


        # STUDENT
        self.label2 = Label(self.frame, text="STUDENT ID :")
        self.label2.config(font=("Times", 15, 'bold'))
        self.label2.place(x=150, y=225)

        self.bid = Entry(self.frame, font="Arial 15")
        self.bid.place(x=350, y=225)
        

        self.but = Button(self.frame, text='GET DATA', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.studentid)
        self.but.place(x=350, y=275)


        # List box
        self.label2 = Label(self.frame, text="BOOK ID :")
        self.label2.config(font=("Times", 15, 'bold'))
        self.label2.place(x=700, y=15)

        self.booklist = Listbox(self.frame, selectmode = "multiple", width=25, height=12)
        self.booklist.config(font=("Times", 14))
        self.booklist.place(x=650,y=75)


        self.label = Label(self.frame, text="For Return The Book Select bookid from listbox and press submit button", fg='red')
        self.label.config(font=("Times", 12))
        self.label.place(x=150, y=380)


        self.but = Button(self.frame, text='<< GO TO Menu', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=150, y=430)

        self.but = Button(self.frame, text=' SUBMIT >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.submit)
        self.but.place(x=600, y=430)

        self.win.mainloop()


    def submit(self):
        sid=self.bid.get()
        tim = date.today()
        selected_item= self.booklist.curselection()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            for item in selected_item:
                bid = self.booklist.get(item)

                cursor.execute("UPDATE booklead SET lead_status=%s,return_time=%s WHERE book_id=%s AND student_id=%s",(1,tim,bid[0],sid))
            conn.commit()
            conn.close()
            mbx.showinfo('SucessFull','Selected Book Has Been Submit.')
        except:
            mbx.showerror('Server Error',"Can Not connect Database. Please try again.")




    def leadid(self):
        lead_id = self.sid.get()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            try:
                cursor.execute(f"SELECT book_id,student_id FROM booklead where id={lead_id} AND lead_status=0")
                book = cursor.fetchall()
                conn.close()
                self.booklist.delete(0, END)
                self.booklist.insert(END, book[0][0])
                self.bid.delete(0, END)
                self.bid.insert(0, book[0][1])
            except:
                mbx.showinfo('Not Found',f'Lending ID {lead_id} has been not found.')
        except:
            mbx.showinfo('Failed','Can not connect to database. Try Again')

    def studentid(self):
        stu_id = self.bid.get()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(f"SELECT book_id FROM booklead where student_id={stu_id} AND lead_status=0")
            book = cursor.fetchall()
            if book:
                conn.close()
                self.booklist.delete(0, END)
                for i in book:
                    self.booklist.insert(END, i)
            else:
                mbx.showinfo('Not Found',f"Student Id {stu_id} has been not lead any book.")
        except:
            mbx.showinfo('Failed','Can not connect to database. Try Again')

    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()
