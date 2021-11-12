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
        self.win.title(" BOOL LENDING | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image = ImageTk.PhotoImage(Image.open("image\lmsdb.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()


        self.label = Label(self.frame, text="LENDING BOOKS", fg='black')
        self.label.config(font=("helvetica", 20))
        self.label.place(x=350, y=10)

        # student 
        self.label1 = Label(self.frame, text="STUDENT ID :")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=150, y=125)

        self.sid = Entry(self.frame, font="Arial 15")
        self.sid.place(x=350, y=125)

        # book
        self.label2 = Label(self.frame, text="BOOK ID :")
        self.label2.config(font=("Times", 15, 'bold'))
        self.label2.place(x=150, y=175)

        self.bid = Entry(self.frame, font="Arial 15")
        self.bid.place(x=350, y=175)

        # Add and remove from list 
        self.but = Button(self.frame, text=' ADD  ', width=8, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.listadd)
        self.but.place(x=350, y=225)

        self.but = Button(self.frame, text='REMOVE', width=8, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.listdel)
        self.but.place(x=475, y=225)


        self.bookid=[]
        # List box
        self.booklist = Listbox(self.frame, width=25, height=15)
        self.booklist.config(font=("Times", 14))
        self.booklist.place(x=650,y=50)
        self.booklist.bind('<<ListboxSelect>>', self.getElement)


        



        self.but = Button(self.frame, text='<< GO TO Menu', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=150, y=430)

        self.but = Button(self.frame, text=' SUBMIT >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.submit)
        self.but.place(x=600, y=430)

        self.win.mainloop()


    def submit(self):
        sid=self.sid.get()
        bid = self.bookid
        tim = date.today()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(f"SELECT RegNo FROM student where id={sid}")
            avi = cursor.fetchone()
            if avi:
                for ci in bid:
                    if ci!='':
                        cursor.execute(f"SELECT totalPage FROM book where id={ci}")
                        bvi=cursor.fetchone()
                        if bvi:
                            cursor.execute(f"SELECT id FROM booklead where book_id={ci} AND student_id={sid} AND lead_status=0")
                            df = cursor.fetchone()
                            if df:
                                mbx.showinfo('warning',f'You have already leaded this book {ci}')
                            else:
                                cursor.execute("INSERT INTO booklead(student_id,book_id,lead_time,lead_status) VALUES(%s,%s,%s,%s)",(sid,ci,tim,0))
                        else:
                            mbx.showinfo('NOt Found',f''' Book Id "{ci}" has been not found''')
                mbx.showinfo('Fun', "Your Data Processed with out any error.")
                        
            else:
                mbx.showinfo('Not Found','Student Id Not found')

            conn.commit()
            conn.close()
        except:
            mbx.showerror('Server Error',"Can Not connect Database. Please try again.")



    def getElement(self, event):
        selection = event.widget.curselection()
        self.index = selection[0]


    def listadd(self):
        self.booklist.insert(END,self.bid.get())
        self.bookid.append(self.bid.get())

    def listdel(self):
        try:
            self.booklist.delete(self.booklist.curselection())
            self.bookid.pop(self.index)
        except:
            pass

    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()
