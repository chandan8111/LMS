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
        self.win.title(" VIEW STUDENT DATA | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image=ImageTk.PhotoImage(Image.open("image\lmsdb.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        self.label = Label(self.frame, text="VIEW STUDENT DATA", fg='black')
        self.label.config(font=("helvetica", 18, 'bold'))
        self.label.place(x=350, y=5)

        
        self.tr = Treeview(self.frame, columns=('A', 'B', 'C', 'D', 'E', 'F', 'G'), selectmode="extended", height=15)



        self.tr.heading('#0', text='STUDENT_ID')
        self.tr.column('#0', minwidth=0, width=75, stretch=NO)
        self.tr.heading('#1', text='FULL_NAME')
        self.tr.column('#1', minwidth=0, width=150, stretch=NO)
        self.tr.heading('#2', text='REG. NO.')
        self.tr.column('#2', minwidth=0, width=150, stretch=NO)
        self.tr.heading('#3', text='GENDER')
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#4', text='SEMESTER')
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#5', text='DEPARTMENT')
        self.tr.column('#5', minwidth=0, width=75, stretch=NO)
        self.tr.heading('#6', text='PHONE_NO')
        self.tr.column('#6', minwidth=0, width=100, stretch=NO)
        self.tr.heading('#7', text='EMAIL')
        self.tr.column('#7', minwidth=0, width=150, stretch=NO)


        self.tr.place(x=25, y=100)


        try:
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            cursor.execute(f"SELECT id,Sname,RegNo,Gender,Sem,Dept,MobNo,Email FROM student")
            mydata=cursor.fetchall()
            conn.close()
            j=0
            for i in mydata:
                self.tr.insert('', index=j, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                j += 1

        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")



        self.but = Button(self.frame, text='GO TO Menu >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=125, y=480)

        self.win.mainloop()
    

    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()

