from tkinter import *
import tkinter as tk
import dashboard
from PIL import ImageTk, Image
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as mbx 


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
        self.win.title(" Search Student Data | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image=ImageTk.PhotoImage(Image.open("image\lmsl.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        self.label = Label(self.frame, text="SEARCH STUDENT", fg='black')
        self.label.config(font=("helvetica", 18, 'bold'))
        self.label.place(x=350, y=5)

        # Label and Entry Field
        self.label1=Label(self.frame, text="Name")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=50)
        self.name=Entry(self.frame, font="Times 12", width=25)
        self.name.place(x=250, y=50)

        # roll no
        self.label1=Label(self.frame, text="Roll No.")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=100)
        self.rollno=Entry(self.frame, font="Times 12", width=25)
        self.rollno.place(x=250, y=100)

        # Branch
        self.label1=Label(self.frame, text="Reg. No.")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=150)
        self.regno=Entry(self.frame, font="Times 12", width=25)
        self.regno.place(x=250, y=150)

        # DOB 
        self.label1=Label(self.frame, text="Date of Birth")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=200)
        self.dob=Entry(self.frame, font="Times 12", width=25)
        self.dob.place(x=250, y=200)
        # Topic
        self.label1=Label(self.frame, text="Mobile No.")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=250)
        self.mobno=Entry(self.frame, font="Times 12", width=25)
        self.mobno.place(x=250, y=250)
        # MObile No.
        self.label1=Label(self.frame, text="Favorite Topics")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=300)
        self.topic=Entry(self.frame, font="Times 12", width=35)
        self.topic.place(x=250, y=300)
        # Email
        self.label1=Label(self.frame, text="Email ID")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=350)
        self.email=Entry(self.frame, font="Times 12", width=35)
        self.email.place(x=250, y=350)
        # Address
        self.label1=Label(self.frame, text="Address")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=50, y=400)
        self.addres=Entry(self.frame, font="Times 12", width=35)
        self.addres.place(x=250, y=400)

        # Student Id
        self.label1=Label(self.frame, text="Student ID")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=550, y=50)
        self.stdid=Entry(self.frame, font="Times 12", width=18)
        self.stdid.place(x=720, y=50)

        # Gender
        self.label3 = Label(self.frame, text="GENDER")
        self.label3.config(font=("Times", 14, 'bold'))
        self.label3.place(x=550, y=100)

        self.gen=Entry(self.frame, font="Times 12", width=18)
        self.gen.place(x=720, y=100)

        # semester 
        self.label4 = Label(self.frame, text="SEMESTER")
        self.label4.config(font=("Times", 14, 'bold'))
        self.label4.place(x=550, y=150)

        self.sem=Entry(self.frame, font="Times 12", width=18)
        self.sem.place(x=720, y=150)

        # Branch
        self.label5 = Label(self.frame, text="DEPARTMENT")
        self.label5.config(font=("Times", 14, 'bold'))
        self.label5.place(x=550, y=200)

        self.dept=Entry(self.frame, font="Times 12", width=18)
        self.dept.place(x=720, y=200)


        self.label7 = Label(self.frame, text="Enter Student id or email or \nreg. no. and press View Button", fg='red')
        self.label7.config(font=("Poppins", 10, 'underline bold'))
        self.label7.place(x=620, y=300)


        self.but = Button(self.frame, text='GO TO Menu >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=125, y=480)
        
        self.but = Button(self.frame, text='Search By ID', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.byid)
        self.but.place(x=625, y=380)

        self.but = Button(self.frame, text='Search By Email', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.byemail)
        self.but.place(x=625, y=430)

        self.but = Button(self.frame, text='Search By Reg. No.', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.byregno)
        self.but.place(x=625, y=480)

        self.win.mainloop()
    
    def byid(self):
        Studenrid= self.stdid.get()
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='lms',user='root',password='Maya@786')
            cursor = conn.cursor()
            cursor.execute(f"SELECT Sname,RollNo,RegNo,Gender,Sem,DOB,Topic,Dept,MobNo,Email,Locat FROM student where id={Studenrid}")
            mydata=cursor.fetchall()
            self.name.delete(0, END)
            self.name.insert(0, mydata[0][0])

            self.rollno.delete(0, END)
            self.rollno.insert(0, mydata[0][1])

            self.regno.delete(0, END)
            self.regno.insert(0, mydata[0][2])

            self.gen.delete(0, END)
            self.gen.insert(0, mydata[0][3])

            self.sem.delete(0, END)
            self.sem.insert(0, mydata[0][4])

            self.dob.delete(0, END)
            self.dob.insert(0, mydata[0][5])

            self.topic.delete(0, END)
            self.topic.insert(0, mydata[0][6])

            self.dept.delete(0, END)
            self.dept.insert(0, mydata[0][7])

            self.mobno.delete(0, END)
            self.mobno.insert(0, mydata[0][8])

            self.email.delete(0, END)
            self.email.insert(0, mydata[0][9])

            self.addres.delete(0, END)
            self.addres.insert(0, mydata[0][10])

            conn.close()

        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")

    def byemail(self):
        Studenremail= self.email.get()
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='lms',user='root',password='Maya@786')
            cursor = conn.cursor()
            cursor.execute(f"SELECT Sname,RollNo,RegNo,Gender,Sem,DOB,Topic,Dept,MobNo, id,Locat FROM student where Email='{Studenremail}'")
            mydata=cursor.fetchall()
            self.name.delete(0, END)
            self.name.insert(0, mydata[0][0])

            self.rollno.delete(0, END)
            self.rollno.insert(0, mydata[0][1])

            self.regno.delete(0, END)
            self.regno.insert(0, mydata[0][2])

            self.gen.delete(0, END)
            self.gen.insert(0, mydata[0][3])

            self.sem.delete(0, END)
            self.sem.insert(0, mydata[0][4])

            self.dob.delete(0, END)
            self.dob.insert(0, mydata[0][5])

            self.topic.delete(0, END)
            self.topic.insert(0, mydata[0][6])

            self.dept.delete(0, END)
            self.dept.insert(0, mydata[0][7])

            self.mobno.delete(0, END)
            self.mobno.insert(0, mydata[0][8])

            self.stdid.delete(0, END)
            self.stdid.insert(0, mydata[0][9])

            self.addres.delete(0, END)
            self.addres.insert(0, mydata[0][10])

            conn.close()

        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")

    def byregno(self):
        Studenri= self.regno.get()
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='lms',user='root',password='Maya@786')
            cursor = conn.cursor()
            cursor.execute(f"SELECT Sname,RollNo,id,Gender,Sem,DOB,Topic,Dept,MobNo,Email,Locat FROM student where RegNo='{Studenri}'")
            mydata=cursor.fetchall()
            self.name.delete(0, END)
            self.name.insert(0, mydata[0][0])

            self.rollno.delete(0, END)
            self.rollno.insert(0, mydata[0][1])

            self.stdid.delete(0, END)
            self.stdid.insert(0, mydata[0][2])

            self.gen.delete(0, END)
            self.gen.insert(0, mydata[0][3])

            self.sem.delete(0, END)
            self.sem.insert(0, mydata[0][4])

            self.dob.delete(0, END)
            self.dob.insert(0, mydata[0][5])

            self.topic.delete(0, END)
            self.topic.insert(0, mydata[0][6])

            self.dept.delete(0, END)
            self.dept.insert(0, mydata[0][7])

            self.mobno.delete(0, END)
            self.mobno.insert(0, mydata[0][8])

            self.email.delete(0, END)
            self.email.insert(0, mydata[0][9])

            self.addres.delete(0, END)
            self.addres.insert(0, mydata[0][10])

            conn.close()

        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")


    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()