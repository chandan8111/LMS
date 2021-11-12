from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as mbx 
import main
import loginPage
import random
import pickle
# for email
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector
from mysql.connector import Error
import time
import dashboard
from store import config
class loginWindow:
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
        self.win.title("REGISTER | LIBRARY MANAGEMENT SYSTEM |")
    
    def add_content(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)
        # x, y = 70, 20

        self.image = ImageTk.PhotoImage(Image.open("image\lmsl.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        self.label = Label(self.frame, text="LIBRARIAN REGISTRATION", fg='black')
        self.label.config(font=("helvetica", 18, 'bold'))
        self.label.place(x=300, y=5)

        # Owner name
        self.label1=Label(self.frame, text="Owner Name")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=200, y=75)
        self.ownername=Entry(self.frame, font="Times 12", width=30)
        self.ownername.place(x=450, y=75)

        # Select liberary
        self.label3 = Label(self.frame, text="Library Name")
        self.label3.config(font=("Times", 14, 'bold'))
        self.label3.place(x=200, y=125)

        self.lib_name=Entry(self.frame, font="Times 12", width=30)
        self.lib_name.place(x=450, y=125)

        # Gender
        self.label3 = Label(self.frame, text="Password")
        self.label3.config(font=("Times", 14, 'bold'))
        self.label3.place(x=200, y=175)
        self.Password=Entry(self.frame, font="Times 12", width=30)
        self.Password.place(x=450, y=175)

        # MObile No.
        self.label1=Label(self.frame, text="Mobile No")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=200, y=225)
        self.lmobno=Entry(self.frame, font="Times 12", width=30)
        self.lmobno.place(x=450, y=225)
        # Email
        self.label1=Label(self.frame, text="Email ID")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=200, y=275)
        self.lemail=Entry(self.frame, font="Times 12", width=30)
        self.lemail.place(x=450, y=275)

        self.label7 = Label(self.frame, text="All fields are mandatory...!", fg='red')
        self.label7.config(font=("Poppins", 11, 'underline bold'))
        self.label7.place(x=320, y=310)

        self.otpbut = Button(self.frame, text='Send OTP', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.sendotp)
        self.otpbut.place(x=350, y=350)

        # OTP ENTER
        self.label1=Label(self.frame, text="Admin OTP")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=150, y=400)
        self.otp=Entry(self.frame, font="Times 15", width=10)
        self.otp.place(x=300, y=400)

        self.label1=Label(self.frame, text="Client OTP")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=450, y=400)
        self.otp2=Entry(self.frame, font="Times 15", width=10)
        self.otp2.place(x=600, y=400)

        self.but = Button(self.frame, text='Submit', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.fsubmit)
        self.but.place(x=350, y=450)



        self.but = Button(self.frame, text='Back >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.go_Back)
        self.but.place(x=45, y=480)

        self.but = Button(self.frame, text='GO TO LOGIN >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.loginPage)
        self.but.place(x=720, y=480)


        self.win.mainloop()

    def go_Back(self):
        self.win.destroy()
        objl = main.Welcome()
        objl.add_content()

    def loginPage(self):
        self.win.destroy()
        lobj = loginPage.loginWindow()
        lobj.add_content()

    def sendotp(self):
        self.genotp = random.randrange(111111,999999,1)
        self.genotp2 = random.randrange(111111,999999,1)
        self.ownername.config(state=DISABLED)
        self.lib_name.config(state=DISABLED)
        self.Password.config(state=DISABLED)
        self.lmobno.config(state=DISABLED)
        self.lemail.config(state=DISABLED)
        client_name=self.ownername.get()
        libr_name=self.lib_name.get()
        client_email=self.lemail.get()
        subject=f"{client_name} Account Otp"
        content = f"{client_name} Registration Otp. Library name {libr_name}. His otp is {self.genotp}"
        content2 = f"{client_name} Registration Otp. Library name {libr_name}. His otp is {self.genotp2}"
        try:
            self.otpbut.config(state=DISABLED)
            # for content one
            message = MIMEMultipart()
            message['From'] = 'lmsp275@gmail.com'
            message['To'] = 'bestangleon@gmail.com'
            message['Subject'] = subject
            message.attach(MIMEText(content, 'plain'))
            # FOR 2
            message1 = MIMEMultipart()
            message1['From'] = 'lmsp275@gmail.com'
            message1['To'] = client_email
            message1['Subject'] = subject
            message1.attach(MIMEText(content2, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('lmsp275@gmail.com', 'LMS@2ndsem')
            text=message.as_string()
            text1=message1.as_string()
            server.sendmail('lmsp275@gmail.com', 'bestangleon@gmail.com',text)
            server.sendmail('lmsp275@gmail.com', client_email,text)
        except:
            self.popt=mbx.showwarning(title="About otp", message="Somthing Wrong. Check your Email Id and try Again")
            self.otpbut.config(state=NORMAL)
        else:
            server.quit()
            self.popt=mbx.showinfo(title="About otp", message="succesfully send otp. For OTP contact the Software Manager or library Manager ")
            self.otpbut.config(state=NORMAL)
        


    def fsubmit(self):
        owner=self.ownername.get()
        library=self.lib_name.get()
        passw=self.Password.get()
        mob=self.lmobno.get()
        email=self.lemail.get()
        if((str(self.genotp)==self.otp.get())and(str(self.genotp2)==self.otp2.get())):
            try:
                conn = mysql.connector.connect(**config)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO librarian(O_Name,L_Name,L_Password,L_MobNo,L_Email) VALUES(%s,%s,%s,%s,%s)",(owner,library,passw,mob,email))
                conn.commit()
                conn.close()
                mbx.showinfo('Sucessfull',"Your Data Has Been Added.")
                time.sleep(3)
                fname=open("data.bin", 'wb')
                num=[email,passw]
                pickle.dump(num, fname)
                fname.close()
                self.win.destroy()
                sh=dashboard.dashBoard()
                sh.add_menu()
            except Error:
                mbx.showwarning("Server Error","Please Try Again After Restart")

        else:
            mbx.showwarning("OTP","Plese Check again your otp")
