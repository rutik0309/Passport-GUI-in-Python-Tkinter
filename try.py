from tkinter.ttk import Combobox
from tkinter import *
import sqlite3 as db

class appoint():

    def __init__(self):
        self.app=Tk()
        self.app.maxsize(900,700)
        self.app.minsize(900,700)
        self.app.title('Passport Seva')
        font11 = "-family Calibri -size 15 -weight bold -slant roman "  \
                "-underline 0 -overstrike 0"
        self.v=StringVar()
            
        Label(self.app,text="Appointment Availability",font="Calibri 26",fg="blue").place(x=20,y=10)
        Label(self.app,text="Passport Office",font="Arial 18").place(x=20,y=100)
        city=['Amritsar','Bhopal','Chandigarh','Chennai','Delhi','Goa','Hyderabad','Jaipur','Jammu','Kolkata','Lucknow','Mumbai','Ranchi','Shimla','Trivandrum','Visakhapatnam']
        TCombobox1 = Combobox(self.app,values=city,takefocus="",textvariable=self.v,font=font11)
        TCombobox1.configure(state="readonly")
        TCombobox1.place(x=200,y=100, relheight=0.051, relwidth=0.280)
        TCombobox1.bind("<<ComboboxSelected>>",self.fetch)
        self.app.mainloop()
        
    def fetch(self,appl):
        self.fr1=Frame(self.app,height=600,width=900,bg='peach puff')
        self.fr1.place(x=0,y=135)
        self.ele=self.v.get()
        print(self.ele)
        print("Database Opened")
        self.conn=db.connect('Appointment.db')
        self.cur=self.conn.cursor()
        self.cur.execute("select * from avail where Location = ?",(self.ele,))
        self.value=self.cur.fetchall()
        self.yo=5
        for i in self.value:
            Label(self.fr1,text=('Location=',i[0]),font="Arial 14",bg="peach puff").place(x=0,y=self.yo)
            self.yo+=30
            Label(self.fr1,text=('Address=',i[1]),font="Arial 14",bg="peach puff").place(x=0,y=self.yo)
            self.yo+=30
            Label(self.fr1,text=('Application_Type=',i[2]),font="Arial 14",bg="peach puff").place(x=0,y=self.yo)
            self.yo+=30
            Label(self.fr1,text=('Appointment_Quota=',i[3]),font="Arial 14",bg="peach puff").place(x=0,y=self.yo)
            self.yo+=30
            Label(self.fr1,text=('Appointment_Date=',i[4]),font="Arial 14",bg="peach puff").place(x=0,y=self.yo)
            self.yo+=30
            Label(self.fr1,text=('Appointments_Released=',i[5]),font="Arial 14",bg="peach puff").place(x=0,y=self.yo)
            self.yo+=40
        self.conn.close()

appoint()
