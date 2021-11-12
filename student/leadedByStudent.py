from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import dashboard
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as mbx 
from store import config

class studentWindow:
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
        self.win.title(" BOOK LENDING DETAILS | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image=ImageTk.PhotoImage(Image.open("image\lmsdb.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        self.label = Label(self.frame, text="BOOK LENDING DETAILS", fg='black')
        self.label.config(font=("helvetica", 18, 'bold'))
        self.label.place(x=300, y=5)

        # Check Button
        self.label1=Label(self.frame, text="STUDENT ID:")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=150, y=50)
        self.sid=Entry(self.frame, font="Times 15", width=8)
        self.sid.place(x=300, y=50)
        self.but = Button(self.frame, text='Check', width=8, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"),command=self.studentid)
        self.but.place(x=400, y=50)

        self.label1=Label(self.frame, text="BOOK ID:")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=500, y=50)
        self.bid=Entry(self.frame, font="Times 15", width=8)
        self.bid.place(x=615, y=50)
        self.but1 = Button(self.frame, text='Check', width=8, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"),command=self.bookid)
        self.but1.place(x=715, y=50)

        # table show
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D', 'E'), selectmode="extended", height=15)

        self.tr.heading('#0', text='LEND ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='STUDENT ID')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='BOOK ID')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='ISSUE DATE')
        self.tr.column('#3', minwidth=0, width=125, stretch=NO)
        self.tr.heading('#4', text='RETURN DATE')
        self.tr.column('#4', minwidth=0, width=125, stretch=NO)
        self.tr.heading('#5', text='LEND STATUS')
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)


        self.tr.place(x=150, y=100)


        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM booklead")
            mydata=cursor.fetchall()
            conn.close()
            j=0
            for i in mydata:
                self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], 'Returned' if (i[5]==1) else '-----'))
                j += 1

        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")



        self.but = Button(self.frame, text='GO TO Menu >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=125, y=480)

        self.win.mainloop()
    
    def studentid(self):
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D', 'E'), selectmode="extended", height=15)

        self.tr.heading('#0', text='LEND ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='STUDENT ID')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='BOOK ID')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='ISSUE DATE')
        self.tr.column('#3', minwidth=0, width=125, stretch=NO)
        self.tr.heading('#4', text='RETURN DATE')
        self.tr.column('#4', minwidth=0, width=125, stretch=NO)
        self.tr.heading('#5', text='LEND STATUS')
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)


        self.tr.place(x=150, y=100)
        sid = self.sid.get()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM booklead WHERE student_id={sid}")
            mydata=cursor.fetchall()
            conn.close()
            j=0
            for i in mydata:
                self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], 'Returned' if (i[5]==1) else '-----'))
                j += 1

        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")

    def bookid(self):
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D', 'E'), selectmode="extended", height=15)

        self.tr.heading('#0', text='LEND ID')
        self.tr.column('#0', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#1', text='STUDENT ID')
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#2', text='BOOK ID')
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#3', text='ISSUE DATE')
        self.tr.column('#3', minwidth=0, width=125, stretch=NO)
        self.tr.heading('#4', text='RETURN DATE')
        self.tr.column('#4', minwidth=0, width=125, stretch=NO)
        self.tr.heading('#5', text='LEND STATUS')
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)


        self.tr.place(x=150, y=100)
        bid = self.bid.get()
        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM booklead WHERE book_id={bid}")
            mydata=cursor.fetchall()
            conn.close()
            j=0
            for i in mydata:
                self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], 'Returned' if (i[5]==1) else '-----'))
                j += 1

        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")
        self.win.mainloop()

    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()
