from tkinter import *
import dashboard
import dashboard
from tkhtmlview import HTMLLabel
class Window:
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
        self.win.title(" ABOUT | LIBRARY MANAGEMENT SYSTEM |")
    def addframe(self):
        self.frame = Frame(self.win, height=540, width=960)
        self.frame.place(x=0, y=0)


        self.ht = HTMLLabel(self.frame, width=119, height=100,html='''
        <section
  style=" float: none; width: 100%"
>
  <div
    style="
      max-width: 1366px;
      position: relative;
      background-color: #2d3035;
      min-height: 1px;
    "
  >
    <h1
      style="
        font-size: 27px;
        font-family: Poppins;
        font-weight: 400;
        color: #ff0000;
        margin: 0;
        padding-bottom: 50px;
        text-align: center;
      "
    >
      OUR TEAM
    </h1>
    <div
      style="
        width: 100px;
        position: relative;
        left: 35%;
        transform: translateX(-50%);
        margin: auto;
        width: 100%;
        float: left;
        display: flex;
        padding: 20px 15px;
      "
    >
      <div
        style="
          width: 400px;
          display: block;
          margin: 1px auto;
          border-radius: 50%;
          background-color: #2d3035;
          border-radius: 8px;
          transition: margin 1s ease, box-shadow 1s ease;
        "
      > 
        <h4
          style="
            font-size: 20px;
            font-family: Poppins;
            margin: 20px 0px 10px;
            color: #ea5e71;
            text-align: center;
            font-weight: 700;
          "
        >
          CHANDAN KUMAR
        </h4>
        <h5
          style="
            font-size: 16px;
            font-family: open sans;
            font-weight: 600;
            color: #b9b9b9;
            margin: 0px 0px 15px;
            text-align: center;
          "
        >
          Reg. No. : 12112785
        </h5>
        <p
          style="
            color: #b9b9b9;
            font-size: 15px;
            font-family: open sans;
            font-weight: 400;
            line-height: 24px;
            text-align: center;
            padding: 0px 20px;
          "
        >
          3rd SEMESTER<br />
          COMPUTER SCIENCE AND ENGINEERING<br />
          LOVELY PROFESSIONAL UNIVERSITY<br /><a href="mailto:chandanpanchi811103@gmail.com">chandanpanchi811103@gmail.com</a><br /><u
            >8298737899</u
          >
        </p>
      </div>
    </div>
    <div
      style="
        width: 100px;
        position: relative;
        left: 35%;
        transform: translateX(-50%);
        margin: auto;
        width: 100%;
        float: left;
        display: flex;
        padding: 20px 15px;
      "
    >
      <div
        style="
          width: 400px;
          display: block;
          margin: 1px auto;
          border-radius: 50%;
          padding: 30px;
          background-color: #2d3035;
          border-radius: 8px;
          transition: margin 1s ease, box-shadow 1s ease;
        "
      >
        <h4
          style="
            font-size: 20px;
            font-family: Poppins;
            margin: 20px 0px 10px;
            color: #ea5e71;
            text-align: center;
            font-weight: 700;
          "
        >
          Yerraguntla Dinakar Raj
        </h4>
        <h5
          style="
            font-size: 16px;
            font-family: open sans;
            font-weight: 600;
            color: #b9b9b9;
            margin: 0px 0px 15px;
            text-align: center;
          "
        >
          Reg. No. : 12020310
        </h5>
        <p
          style="
            color: #b9b9b9;
            font-size: 15px;
            font-family: open sans;
            font-weight: 400;
            line-height: 24px;
            text-align: center;
            padding: 0px 20px;
          "
        >
          3rd SEMESTER<br />
          COMPUTER SCIENCE AND ENGINEERING<br />
          LOVELY PROFESSIONAL UNIVERSITY<br /><a href="mailto:dinakarraj10@gmail.com">dinakarraj10@gmail.com</a><br />
          <u>7075225245</u>
        </p>
      </div>
    </div>
  </div>
</section>

        ''')
        self.ht.place(x=0,y=0)


        self.but = Button(self.frame, text='GO TO Menu >>', width=18, bg='light grey', fg='black',
                          font=("Poppins", 12, " bold"), command=self.gotoDash)
        self.but.place(x=100, y=500)

        self.win.mainloop()
    

    def gotoDash(self):
        self.win.destroy()
        dh = dashboard.dashBoard()
        dh.add_menu()
