from tkinter import *
import tkinter as tk
import dashboard   
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
        self.win.title(" STUDENT REGISTRATION | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)

        self.image = ImageTk.PhotoImage(Image.open("image\lmsdb.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        self.label = Label(self.frame, text="NEW STUDENT REGISTRATION", fg='black')
        self.label.config(font=("helvetica", 18, 'bold'))
        self.label.place(x=280, y=5)

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

        # Gender
        self.label3 = Label(self.frame, text="GENDER")
        self.label3.config(font=("Times", 14, 'bold'))
        self.label3.place(x=550, y=50)

        self.gender = ['None', 'Male', 'Female', 'Other']
        self.gen = tk.StringVar(self.frame)
        self.droplist = tk.OptionMenu(self.frame, self.gen, *self.gender)
        self.droplist.config(width=17)
        self.gen.set(self.gender[0])
        self.droplist.place(x=720, y=50)

        # semester 
        self.label4 = Label(self.frame, text="SEMESTER")
        self.label4.config(font=("Times", 14, 'bold'))
        self.label4.place(x=550, y=100)

        self.semester = ['None', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth','Other']
        self.sem = tk.StringVar(self.frame)
        self.droplist = tk.OptionMenu(self.frame, self.sem, *self.semester)
        self.droplist.config(width=17)
        self.sem.set(self.semester[0])
        self.droplist.place(x=720, y=100)

        # Branch
        self.label5 = Label(self.frame, text="DEPARTMENT")
        self.label5.config(font=("Times", 14, 'bold'))
        self.label5.place(x=550, y=150)

        self.list = ["NONE",
                     "CSE",
                     "ISE",
                     "ME",
                     "CIV",
                     "EEE",
                     "ECE",
                     "Other"]
        self.dept = tk.StringVar(self.frame)
        self.drop = tk.OptionMenu(self.frame, self.dept, *self.list)
        self.drop.config(width=17)
        self.dept.set(self.list[0])
        self.drop.place(x=720, y=150)



        self.label7 = Label(self.frame, text="", fg='white')
        self.label7.config(font=("Poppins", 10, 'underline bold'))
        self.label7.place(x=620, y=400)


        self.but = Button(self.frame, text='GO TO Menu >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=125, y=480)

        self.but = Button(self.frame, text='Submit >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.addStudent)
        self.but.place(x=625, y=480)

        self.win.mainloop()
    
    def addStudent(self):
        data=(
            self.name.get(),
            self.rollno.get(),
            self.regno.get(),
            self.gen.get(),
            self.sem.get(),
            self.dept.get(),
            self.dob.get(),
            self.topic.get(),
            self.mobno.get(),
            self.email.get(),
            self.addres.get()
        )
        try:
            conn = mysql.connector.connect(host='127.0.0.1',database='lms',user='root',password='Maya@786')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO student(Sname,RollNo,RegNo,Gender,Sem,DOB,Topic,Dept,MobNo,Email,Locat) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(data[0],data[1],data[2],data[3],data[4],data[6],data[7],data[5],data[8],data[9],data[10]))
            conn.commit()
            mbx.showinfo('Sucessfull',"Your Data Has Been Added.")
        except Error:
            mbx.showwarning("Server Error","Please Try Again After Restart")


    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()