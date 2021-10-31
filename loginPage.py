from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbx 
import main
import registerPage
import dashboard
import pickle
import os
import mysql.connector
from mysql.connector import Error

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


        self.image = ImageTk.PhotoImage(Image.open("image\lmsl.jpg"))
        self.label = Label(self.frame, image=self.image)
        self.label.pack()

        # creating login form for only admin can access
        self.label = Label(self.frame, text="USER LOGIN")
        self.label.config(font=("Courier", 20, 'underline bold'))
        self.label.place(x=380, y=180)

        # creating username label and entry field
        self.label1 = Label(self.frame, text="USERNAME")
        self.label1.config(font=("Times", 16, 'bold'))
        self.label1.place(x=240, y=250)

        self.user = Entry(self.frame, font="Times 12")
        self.user.place(x=385, y=250)

        # creating password label and entry field
        self.label2 = Label(self.frame, text="PASSWORD")
        self.label2.config(font=("Times", 16, 'bold'))
        self.label2.place(x=240, y=300)

        self.pswd = Entry(self.frame, font="Times 12", show="*")
        self.pswd.place(x=385, y=300)
        # Checkbox
        self.cbv=IntVar()
        self.checkbox = Checkbutton(self.frame, variable=self.cbv, onvalue=1, offvalue=0, text="Keep me logged in").place(x=382, y=335)

        self.btn = Button(self.frame, text='LOGIN', width=16, bg='light grey', fg='black', font=("Times", 13, "bold"), command=self.login)
        self.btn.place(x=382, y=370)

        self.but = Button(self.frame, text='Back >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.go_Back)
        self.but.place(x=45, y=480)

        self.but = Button(self.frame, text='Delete Saved Password', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.passw)
        self.but.place(x=380, y=480)

        self.but = Button(self.frame, text='GO TO Register >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.registerPage)
        self.but.place(x=720, y=480)

        try:
            fopen=open("data.bin", 'rb')
        except:
            print('')
        else:
            udata=pickle.load(fopen)
            try:
                self.user.delete(0, END)
                self.user.insert(0, udata[0])
                self.pswd.delete(0, END)
                self.pswd.insert(0, udata[1])
            except:
                print('')
            fopen.close()
    
    
    def passw(self):
        try:
            os.remove('data.bin')
            self.add_content()
        except:
            pass

    def login(self):
        if len(self.user.get()) == 0 or len(self.pswd.get())==0:
            mbx.showinfo("INVALID USERNAME OR PASSWORD")
        else:
            try:
                conn = mysql.connector.connect(host='127.0.0.1',database='lms',user='root',password='Maya@786')
                cursor = conn.cursor()
                fuser=self.user.get()
                fpass=self.pswd.get()
                cursor.execute('''Select * from `LIBRARIAN` where L_Email= %s AND L_Password = %s ''',(fuser,fpass))
                pcD = cursor.fetchone()
                if pcD:
                    if self.cbv.get() == 1:
                        fname=open("data.bin", 'wb')
                        num=[self.user.get(),self.pswd.get()]
                        pickle.dump(num, fname)
                        fname.close()
                    else:
                        pass
                    self.win.destroy()
                    sh=dashboard.dashBoard()
                    sh.add_menu()
                else:
                    mbx.showinfo("Login error", "Username and password not found")
            except Error:
                mbx.showinfo('Servor Error', "Something Goes Wrong with server,\n Try restarting")


        self.win.mainloop()

    def go_Back(self):
        self.win.destroy()
        objl = main.Welcome()
        objl.add_content()

    def registerPage(self):
        self.win.destroy()
        robj = registerPage.loginWindow()
        robj.add_content()        