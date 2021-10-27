from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as mbx 
import main
import loginPage
import random

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
        self.win.title("Login | LIBRARY MANAGEMENT SYSTEM |")
    
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
        self.label3 = Label(self.frame, text="GENDER")
        self.label3.config(font=("Times", 14, 'bold'))
        self.label3.place(x=200, y=175)

        self.gender = ['None                                                 ', 'Male', 'Female', 'Other']
        self.gen = tk.StringVar(self.frame)
        self.droplist = tk.OptionMenu(self.frame, self.gen, *self.gender)
        self.droplist.config(width=30)
        self.gen.set(self.gender[0])
        self.droplist.place(x=450, y=175)

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

        self.but = Button(self.frame, text='Send OTP', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.sendotp)
        self.but.place(x=350, y=350)

        # OTP ENTER
        self.label1=Label(self.frame, text="Enter OTP")
        self.label1.config(font=("Times", 15, 'bold'))
        self.label1.place(x=300, y=400)
        self.otp=Entry(self.frame, font="Times 15", width=15)
        self.otp.place(x=450, y=400)

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
        self.popt=mbx.showinfo(title="About otp", message="For OTP contact the Software Manager or library Manager ")
        genotp = random.randrange(111111,999999,1)
        print(genotp)

    def fsubmit(self):
        data=(
            self.ownername.get(),
            self.lib_name.get(),
            self.gen.get(),
            self.lmobno.get(),
            self.lemail.get()
        )