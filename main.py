from tkinter import *
from tkinter import ttk
import sqlite3 
import random
from sqlite3 import *
import string
from tkinter import messagebox
import os
from tkinter.ttk import Combobox
import tkinter.messagebox as msg
import time
import datetime as dt
import calendar
#import file
root = Tk()


with sqlite3.connect("Sample.db") as db:
    cur = db.cursor()

def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def valid_gphone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

'''def string(abc):
    if re.match("[a-b]+)",abc):
        return True
    return False'''
        

user = StringVar()
passwd = StringVar()
passwd2 = StringVar()
fname = StringVar()
surname = StringVar()
gender = StringVar()
birth = StringVar()
father_name = StringVar()
father_surname = StringVar()
g_name = StringVar()
g_surname = StringVar()
mother_name = StringVar()
mother_surname = StringVar()
mobile_num = StringVar()
gmobile_num = StringVar()
address = StringVar()
email = StringVar()
village = StringVar()
marital= StringVar()
cindia= StringVar()
pan= StringVar()
voter= StringVar()
emp= StringVar()
gover= StringVar()
edu= StringVar()
category= StringVar()
mark= StringVar()
adhaar= StringVar()
reg_name= StringVar()
reg_surname= StringVar()
reg_dob= StringVar()
reg_email= StringVar()
reg_id= StringVar()
reg_password= StringVar()
reg_cpassword= StringVar()

def appoint():
    os.system('python try.py')

def login_page():
    global loginn
    global page1
    loginn = Toplevel()
    page1 = Login_Try(loginn)
    loginn.mainloop()

def new_register_page():
    global new_user
    global page2
    new_user = Toplevel()
    page2 = New_Reg_Try(new_user)
    new_user.mainloop()

    
#def appli():
    #global call
    #global form
    #form=Toplevel()
    #page3=Appli(form)
    #form.mainloop()
    

    
def application1():
    global app1
    global page3
    app1 = Toplevel()
    page3 = Application_Form1(app1)
    app1.mainloop()


def application2():
    global app2
    global page4
    app2 = Toplevel()
    page4 = Application_Form2(app2)
    app2.mainloop()


def application3():
    global app3
    global page5
    app3 = Toplevel()
    page5 = Application_Form3(app3)
    app3.mainloop()

def application4():
    global app4
    global page6
    app4 = Toplevel()
    page6 = Application_Form4(app4)
    app4.mainloop()



def application5():
    global app5
    global page7
    app5 = Toplevel()
    page7 = Application_Form5(app5)
    app5.mainloop()

def application6():
    global app6
    global page8
    app6 = Toplevel()
    page8 = Application_Form6(app6)
    app6.mainloop()


    



class Passport:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Calibri -size 30 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font11 = "-family Calibri -size 15 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font14 = "-family Calibri -size 24 -weight bold -slant roman "  \
            "-underline 1 -overstrike 0"

        top.geometry("1024x705+-163+44")
        top.minsize(120, 1)
        top.maxsize(1028, 749)
        top.resizable(1, 1)
        top.title("Passport Seva")
        top.configure(background="#ffd1bb")

        self.Ashoka = Button(top)
        self.Ashoka.place(relx=0.02, rely=0.014, height=201, width=131)
        self.Ashoka.configure(activebackground="#ececec")
        self.Ashoka.configure(activeforeground="#000000")
        self.Ashoka.configure(background="#d9d9d9")
        self.Ashoka.configure(disabledforeground="#a3a3a3")
        self.Ashoka.configure(foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")
        
        global _img0
        _img0 = PhotoImage(file="home images.png")
        self.Ashoka.configure(image=_img0)
        self.Ashoka.configure(pady="0")
        self.Ashoka.configure(text='''Button''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.195, rely=0.326, height=73, width=323)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#cd0532")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#000000")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''New User Registration''')
        self.Button1.configure(command=new_register_page)


        self.Button2 = Button(top)
        self.Button2.place(relx=0.195, rely=0.482, height=74, width=327)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#00a400")
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#000000")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="groove")
        self.Button2.configure(text='''Existing User Login''')
        self.Button2.configure(command=login_page)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.195, rely=0.638, height=74, width=327)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#00b3b3")
        self.Button3.configure(borderwidth="4")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font11)
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#000000")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="groove")
        self.Button3.configure(text='''Check Appointment Availability''')
        self.Button3.configure(command=appoint)

        '''self.Button4 = Button(top)
        self.Button4.place(relx=0.195, rely=0.809, height=74, width=327)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#bbbb00")
        self.Button4.configure(borderwidth="4")
        self.Button4.configure(disabledforeground="#c0c0c0")
        self.Button4.configure(font=font11)
        self.Button4.configure(foreground="#ffffff")
        self.Button4.configure(highlightbackground="#000000")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(relief="groove")
        self.Button4.configure(text=Track Application Status)'''

        self.Label1 = Label(top)
        #self.Label1.place(relx=0.107, rely=0.028, height=61, width=348)
        self.Label1.place(relx=0.166, rely=0.028, height=61, width=230)
        self.Label1.configure(activebackground="#000000")
        self.Label1.configure(activeforeground="white")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#ffd1bb")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(takefocus="")
        self.Label1.configure(text='''Passport Seva''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        

        self.Label2 = Label(top)
        self.Label2.place(relx=0.166, rely=0.113, height=21, width=186)
        self.Label2.configure(background="#ffd1bb")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Consular, Passport & Visa Division''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.166, rely=0.142, height=21, width=260)
        self.Label3.configure(background="#ffd1bb")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Ministry of External Affairs, Government of India''')

        

        self.Button5 = Button(top)
        self.Button5.place(relx=0.684, rely=0.014, height=114, width=306)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        global _img1
        _img1 = PhotoImage(file="home.png")
        self.Button5.configure(image=_img1)
        self.Button5.configure(pady="0")

        self.Label4 = Label(top)
        self.Label4.place(relx=0.703, rely=0.44, height=70, width=298)
        self.Label4.configure(activeforeground="#000000")
        self.Label4.configure(background="#ffd1bb")
        self.Label4.configure(borderwidth="5")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font14)
        self.Label4.configure(foreground="#000075")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="#ffffff")
        self.Label4.configure(text='''Information Corner''')

        self.Button6 = Button(top)
        self.Button6.place(relx=0.703, rely=0.553, height=60, width=296)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#4aa5ff")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font11)
        self.Button6.configure(foreground="#ffffff")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="#000000")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Instruction Booklet''')
        self.Button6.configure(command=instruction)

        self.Button7 = Button(top)
        self.Button7.place(relx=0.703, rely=0.667, height=60, width=298)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#4aa5ff")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font11)
        self.Button7.configure(foreground="#ffffff")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Documents Required for Passport''')
        self.Button7.configure(command=doc_required)

        self.Button8 = Button(top)
        self.Button8.place(relx=0.703, rely=0.78, height=54, width=291)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#4aa4ff")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font=font11)
        self.Button8.configure(foreground="#ffffff")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Show e-Form''')
        self.Button8.configure(command=e_form)

        self.Button9 = Button(top)
        self.Button9.place(relx=0.703, rely=0.879, height=50, width=296)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#4aa5ff")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(font=font11)
        self.Button9.configure(foreground="#ffffff")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Grievance/Feedback''')
        self.Button9.configure(command=feedback)


class Login_Try:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family Calibri -size 20 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family Calibri -size 30 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("864x611+93+370")
        top.minsize(120, 1)
        top.maxsize(1028, 749)
        top.resizable(1, 1)
        top.title("Exisiting User Login")
        top.configure(background="#ffc1c1")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.180, rely=0.327, relheight=0.600, relwidth=0.65)

        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#ff6464")

       

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.165, rely=0.27, height=60, width=141)
        self.Label1.configure(activebackground="#ff6464")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ff6464")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#ffffff")
        self.Label1.configure(text='''Login Id''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.165, rely=0.494, height=61, width=147)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ff6464")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Password''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.436, rely=0.292,height=38, relwidth=0.412)
        self.Entry1.configure(background="#ffffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Calibri} -size 15")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=user)


        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.436, rely=0.517,height=38, relwidth=0.412)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Calibri} -size 15")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(show="*")
        self.Entry2.configure(textvariable=passwd)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.376, rely=0.809, height=54, width=169)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')
        #self.Button1.configure(command=application1)
        self.Button1.configure(command=login)
        #self.Button1.configure(command=appli)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.162, rely=0.0, height=101, width=254)
        self.Label1.configure(background="#ffc1c1")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Passport Seva''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.174, rely=0.131, height=21, width=186)
        self.Label2.configure(background="#ffc1c1")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Consular, Passport & Visa Division''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.162, rely=0.164, height=21, width=276)
        self.Label3.configure(background="#ffc1c1")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Ministry of External Affairs, Government of India''')

        self.Ashoka = Button(top)
        self.Ashoka.place(relx=0.012, rely=0.016, height=204, width=127)
        self.Ashoka.configure(activebackground="#ececec")
        self.Ashoka.configure(activeforeground="#000000")
        self.Ashoka.configure(background="#d9d9d9")
        self.Ashoka.configure(disabledforeground="#a3a3a3")
        self.Ashoka.configure(foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")
        
        global _img2
        _img2 = PhotoImage(file="login images.png")
        self.Ashoka.configure(image=_img2)
        self.Ashoka.configure(pady="0")
        self.Ashoka.configure(text='''Button''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.684, rely=0.014, height=114, width=306)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
     
        global _img3
        _img3 = PhotoImage(file="login download.png")
        self.Button3.configure(image=_img3)
        self.Button3.configure(pady="0")

        


    
def login():
    
    
    username = user.get()
    password = passwd.get()

    find_user = "SELECT * FROM app2 WHERE login = ? and password = ?"
    cur.execute(find_user, [username, password])
    results = cur.fetchall()
    if results:
        messagebox.showinfo("Login Page", "The login is successful")
        page1.Entry1.delete(0, END)
        page1.Entry2.delete(0, END)
        root.withdraw()
        
        global appli
        global page0
        appli = Toplevel()
        page0 = Appli(appli)
        appli.mainloop()
        appli.protocol("WM_DELETE_WINDOW", exitt)
        
    else:
        messagebox.showerror("Error", "Incorrect username or password.")
        page1.Entry2.delete(0, END)

        
    


class New_Reg_Try:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font13 = "-family Calibri -size 9 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family Calibri -size 20 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1024x705+102+71")
        top.minsize(120, 1)
        top.maxsize(1028, 749)
        top.resizable(1, 1)
        top.title("User Registration")
        top.configure(background="#e6ffff")

        
        self.Ashoka = Button(top)
        self.Ashoka.place(relx=0.02, rely=0.014, height=201, width=131)
        self.Ashoka.configure(activebackground="#ececec")
        self.Ashoka.configure(activeforeground="#000000")
        self.Ashoka.configure(background="#d9d9d9")
        self.Ashoka.configure(disabledforeground="#a3a3a3")
        self.Ashoka.configure(foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")
        global _img4
        _img4 = PhotoImage(file="images.png")
        self.Ashoka.configure(image=_img4)
        self.Ashoka.configure(pady="0")


        

        self.Label1 = Label(top)
        self.Label1.place(relx=0.186, rely=0.113, height=40, width=203)
        self.Label1.configure(background="#e6ffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Passport Office''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.176, rely=0.199, height=39, width=123)
        self.Label2.configure(background="#e6ffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Name''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.186, rely=0.27, height=39, width=136)
        self.Label3.configure(background="#e6ffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Surname''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.186, rely=0.355, height=31, width=174)
        self.Label4.configure(background="#e6ffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Date of Birth''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.186, rely=0.426, height=39, width=133)
        self.Label5.configure(background="#e6ffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''E-mail Id''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.195, rely=0.511, height=49, width=103)
        self.Label6.configure(background="#e6ffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Login Id''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.176, rely=0.61, height=62, width=164)
        self.Label7.configure(background="#e6ffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font9)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Password''')

        self.Label8 = Label(top)
        self.Label8.place(relx=0.195, rely=0.695, height=62, width=211)
        self.Label8.configure(background="#e6ffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font9)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Confirm Password''')

        self.Message1 = Message(top)
        self.Message1.place(relx=0.205, rely=0.156, relheight=0.04
                , relwidth=0.187)
        self.Message1.configure(background="#e6ffff")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''(As per Present Residential Address)''')
        self.Message1.configure(width=191)

        self.Message2 = Message(top)
        self.Message2.place(relx=0.273, rely=0.213, relheight=0.04
                , relwidth=0.111)
        self.Message2.configure(background="#e6ffff")
        self.Message2.configure(font=font13)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''(Max 45 Characters)''')
        self.Message2.configure(width=114)

        self.Message3 = Message(top)
        self.Message3.place(relx=0.303, rely=0.284, relheight=0.04
                , relwidth=0.111)
        self.Message3.configure(background="#e6ffff")
        self.Message3.configure(font=font13)
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''(Max 45 Characters)''')
        self.Message3.configure(width=114)

        self.Message4 = Message(top)
        self.Message4.place(relx=0.303, rely=0.44, relheight=0.04
                , relwidth=0.111)
        self.Message4.configure(background="#e6ffff")
        self.Message4.configure(font=font13)
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text='''(Max 35 Characters)''')
        self.Message4.configure(width=114)

        self.Message5 = Message(top)
        self.Message5.place(relx=0.342, rely=0.355, relheight=0.054
                , relwidth=0.087)
        self.Message5.configure(background="#e6ffff")
        self.Message5.configure(font=font13)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(text='''(DD/MM/YYYY)''')
        self.Message5.configure(width=89)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.469, rely=0.213,height=30, relwidth=0.346)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=reg_name)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.469, rely=0.284,height=30, relwidth=0.346)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=reg_surname)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.469, rely=0.44,height=30, relwidth=0.346)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=reg_email)

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.469, rely=0.525,height=30, relwidth=0.346)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        #self.Entry4.configure(textvariable=user)

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.469, rely=0.61,height=30, relwidth=0.346)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(show="*")
        self.Entry5.configure(textvariable=passwd)
        

        self.Entry6 = Entry(top)
        self.Entry6.place(relx=0.469, rely=0.695,height=30, relwidth=0.346)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(show="*")
        self.Entry6.configure(textvariable=passwd2)
        

        self.Entry7 = Entry(top)
        self.Entry7.place(relx=0.469, rely=0.355,height=30, relwidth=0.346)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(textvariable=reg_dob)

        self.Entry8 = Entry(top)
        self.Entry8.place(relx=0.469, rely=0.128,height=30, relwidth=0.346)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.527, rely=0.837, height=66, width=119)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#0067ce")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Clear''')
        self.Button2.configure(command=self.clearr)

        self.Message6 = Message(top)
        self.Message6.place(relx=0.811, rely=0.199, relheight=0.075
                , relwidth=0.177)
        self.Message6.configure(background="#e6ffff")
        self.Message6.configure(font=font13)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''First Name + Middle Name''')
        self.Message6.configure(width=181)

        self.Message7 = Message(top)
        self.Message7.place(relx=0.811, rely=0.482, relheight=0.136
                , relwidth=0.179)
        self.Message7.configure(background="#e6ffff")
        self.Message7.configure(font=font13)
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(text='''Must contain Special characters,Digits and Capital letters''')
        self.Message7.configure(width=183)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.361, rely=0.837, height=66, width=114)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#0067ce")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Register''')
        self.Button3.configure(command=self.fun)
        

    def fun(self):
           
                
            if(reg_name.get()==""):
                messagebox.showerror("Oops!", "Please enter a Name.")
            elif(reg_surname.get()==""):
                messagebox.showerror("Oops!", "Please enter a Surname.")
            elif(reg_dob.get()==""):
                messagebox.showerror("Oops!", "Please select a Date of Birth.")
        
            elif(reg_email.get()==""):
                messagebox.showerror("Oops!", "Please enter E-mail ID.")

            else:
                

                #self.conn = db.connect('Sample.db')
                #cur = self.conn.cursor()
                cur.execute ('''CREATE TABLE IF NOT EXISTS app2
                (
                 Fname TEXT,
                 Lname TEXT,
                 DOB TEXT,
                 Email TEXT,
                 login TEXT,
                 password TEXT,
                 cpassword TEXT
                 )''')

               
            
                cur.execute("insert into app2 values(?,?,?,?,?,?,?)",(self.Entry1.get(),self.Entry2.get(),self.Entry7.get(),self.Entry3.get(),self.Entry4.get(),self.Entry5.get(),self.Entry6.get()))
                cuttr=cur.execute('''SELECT * from app2 ''')
                for data in cuttr:
                    
                    print("Name: ",data[0])
                    print("Surname: ",data[1])
                    print("DATE OF BIRTH: ",data[2])
                    print("EMAIL: ",data[3])
                    print("LOGIN: ",data[4])
                    print("PASSWORD: ",data[5])
                    print("CPASSWORD: ",data[6],'\n')


           
                #self.cur.close()
                db.commit()
                cur.close()

            
            
    def clearr(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry7.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry6.delete(0, END)

class Appli():
    def __init__(self,top=None):
        self.top=top
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        
        top.configure(height=800,width=900,bg='white')
        top.title("Choose Passport type")
        
        
        self.label=Label(top,font=('bold',18),text="Choose Passport type",width=150,anchor=W,bg='light grey')
        self.label.place(x=0,y=130)
        self.lab=Label(top,font=('calibre',18,'bold'),text="Please read the passport instruction booklet carefully before filling the Aplication form.",width=80,bg='white')
        self.la=Label(top,font=('calibre',18,'bold'),text='Furnishing incorrect information would lead to rejection of application.',width=80,bg='white')
        self.la1=Label(top,font=('calibre',18,'bold'),text='Please produce original documents at the time of submission of form.',width=80,bg='white')
        self.la2=Label(top,font=('calibre',18,'bold'),text='Refer documets required section for more details',width=80,bg='white')
        self.lab1=Label(top,font=('calibre',18,'bold'),text='Applying for*',activebackground='#ffffff',bg='white')
        self.lab2=Label(top,font=('calibre',18,'bold'),text='Pages to apply*',activebackground='#ffffff',bg='white')        
        self.lab3=Label(top,font=('calibre',18,'bold'),text='Type of passport booklet*',activebackground='#ffffff',bg='white')
        
        self.label0=Label(top,width=400,anchor=W,bg='light grey')
        self.label0.place(x=0,y=300)
      
        self.lab.place(x=100,y=175)
        self.la.place(x=100,y=208)
        self.la1.place(x=100,y=239)
        self.la2.place(x=100,y=268)
        self.lab1.place(x=100,y=430)
        self.lab2.place(x=100,y=489)        
        self.lab3.place(x=100,y=550)
        self.rad1=Radiobutton(top,font=('calibre',18,'bold'),variable=self.var1,value=1,text='Normal',bg='white')
        self.rad2=Radiobutton(top,font=('calibre',18,'bold'),variable=self.var1,value=2,text='Tatkal ',bg='white')
        self.rad3=Radiobutton(top,font=('calibre',18,'bold'),variable=self.var2,value=1,text='30',bg='white')
        self.rad4=Radiobutton(top,font=('calibre',18,'bold'),variable=self.var2,value=2,text='60',bg='white')
        self.rad5=Radiobutton(top,font=('calibre',18,'bold'),variable=self.var3,value=1,text='Fresh',bg='white')
        self.rad6=Radiobutton(top,font=('calibre',18,'bold'),variable=self.var3,value=2,text='Renew',bg='white')
        self.rad1.place(x=850,y=430)
        self.rad2.place(x=700,y=430)
        self.rad3.place(x=850,y=489)
        self.rad4.place(x=700,y=489)
        self.rad5.place(x=850,y=550)
        self.rad6.place(x=700,y=550)
        self.comm=Button(top,font=('calibre',18,'bold'),bg='light grey',text='Proceed',command=self.deciede)
        self.comm.place(x=305,y=650)
        self.Ashoka = Button(top, height=90, width=57,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")

        global _img0
        _img0 = PhotoImage(file="app1.png")
        self.Ashoka.configure(image=_img0)
 
        self.Ashoka.place(x=8,y=10)
        self.Button4 = Button(top)
        self.Button4.place(x=1200,y=5, height=124, width=307)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        
        global _img1
        _img1 = PhotoImage(file="login download.png")
        self.Button4.configure(image=_img1)
        self.Button4.configure(pady="0")


        self.Label14 = Label(top)
        self.Label14.place(x=120,y=10,height=35, width=245)
        self.Label14.configure(background="#ffffff")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font=('calibre',15))
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Passport Seva''')

        self.Label15 = Label(top)
        self.Label15.place(x=120,y=35,height=21, width=186)
        self.Label15.configure(background="#ffffff")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Consular, Passport & Visa Division''')

        self.Label16 = Label(top)
        self.Label16.place(x=120,y=60,height=21, width=260)
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Ministry of External Affairs, Government of India''')


    def deciede(self):
        type_pag=self.var1.get()
        pages=self.var2.get()   
        chk=self.var3.get()
        print(chk)
        print(type_pag)
        print(pages)
        if chk==0 or type_pag==0 or pages==0:
            messagebox.showerror("Error", "PLEASE SELECT AN OPTION FOR ASTREK MARKED FIELDS.")
        elif chk==2:
            self.choose()
        elif chk==1:
            application1()

            
    def choose(self):
        self.vara1=IntVar()
        
        self.radd1=Radiobutton(self.top,font=('calibre',18,'bold'),variable=self.vara1,value=1,text='Change in Existing Personal Information')
        self.radd2=Radiobutton(self.top,font=('calibre',18,'bold'),variable=self.vara1,value=2,text='Damage Passport/Lost/Exprired')
       
        self.lab=Label(self.top,font=('calibre',18,'bold'),text='*close this window to select fresh option*')
        self.comm=Button(self.top,font=('calibre',18,'bold'),text='Select Option To Proceed',command=self.deciedeit,bg='grey')
        self.comm.place(x=305,y=650)

        self.lab.place(x=850,y=750)
        self.radd1.place(x=850,y=550)
        self.radd2.place(x=850,y=600)
        
    def deciedeit(self):
        if self.vara1.get()==1:
            application1()
        elif self.vara1.get()==2:
            os.system("python file.py")
        elif self.vara1.get()==0:
            messagebox.showerror("Error", "PLEASE SELECT AN OPTION TO CONTINUE FURTHER.")
            #file.application1(root)


       
class Application_Form1():
    
    def __init__(self, top=None,val=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font11 = "-family Calibri -size 16 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family Calibri -size 18 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family Calibri -size 20 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        


        top.geometry("1024x705+102+71")
        top.minsize(120, 1)
        top.maxsize(1028, 729)
        top.resizable(1, 1)
        top.title("Application Form")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#ffffff")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.190, height=41, width=1024)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#c0c0c0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Applicant Details''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.017, rely=0.260, height=51, width=814)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="#ffffff")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Applicant's Given Name (Given Name means First Name followed by middle Name (if any)) *''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.017, rely=0.320,height=43, relwidth=0.9)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#ff0000")
        self.Entry1.configure(font=font12)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(textvariable=fname)
        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.017, rely=0.410, height=32, width=93)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Surname*''')

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.017, rely=0.470,height=43, relwidth=0.9)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font12)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=surname)
        
        self.Label4 = Label(top)
        self.Label4.place(relx=0.017, rely=0.570, height=32, width=80)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Gender*''')




        l=["Male","Female","Transgender"]
        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.150, rely=0.570, relheight=0.051
                , relwidth=0.280)
        self.TCombobox1.configure(values=l)
        self.TCombobox1.configure(font=font11)
        #self.TCombobox1.configure(show="Male,Female,Transgenger")
        #self.TCombobox1.configure(textvariable=application1_support.combobox)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=gender)


        
        self.Label5 = Label(top)
        self.Label5.place(relx=0.014, rely=0.660, height=32, width=280)
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font11)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Date of Birth (DD/MM/YYYY)*''')

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.290, rely=0.660,height=43, relwidth=0.30)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font12)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=birth)

        self.Ashoka = Button(top)
        self.Ashoka.place(relx=0.017, rely=0.0, height=107, width=62)
        self.Ashoka.configure(activebackground="#ececec")
        self.Ashoka.configure(activeforeground="#000000")
        self.Ashoka.configure(background="#ffffff")
        self.Ashoka.configure(disabledforeground="#a3a3a3")
        self.Ashoka.configure(foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")   
        self.Ashoka.configure(highlightcolor="white")
        
        global _img0
        _img0 = PhotoImage(file="app1.png")
        self.Ashoka.configure(image=_img0)
        self.Ashoka.configure(pady="0")
        self.Ashoka.configure(relief="flat")

        self.Label6 = Label(top)
        self.Label6.place(relx=0.08, rely=0.024, height=35, width=145)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font10)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Passport Seva''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.08, rely=0.07, height=21, width=186)
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Consular, Passport & Visa Division''')

        self.Label8 = Label(top)
        self.Label8.place(relx=0.08, rely=0.093, height=21, width=260)
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Ministry of External Affairs, Government of India''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.77, rely=0.022, height=94, width=206)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        

        global _img1
        _img1 = PhotoImage(file="app1 passport.png")
        self.Button2.configure(image=_img1)
        self.Button2.configure(pady="0")


        self.Label9 = Label(top)
        self.Label9.place(relx=0.014, rely=0.760, height=32, width=340)
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font=font11)
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Have you ever changed your name ? *''')

        self.var = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.35, rely=0.750, relheight=0.078
                , relwidth=0.098)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.45, rely=0.750, relheight=0.078
                , relwidth=0.098)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        



        self.Labe20 = Label(top)
        self.Labe20.place(relx=0.60, rely=0.770, height=28, width=300)
        self.Labe20.configure(background="#ffffff")
        self.Labe20.configure(disabledforeground="#a3a3a3")
        self.Labe20.configure(foreground="#000000")
        self.Labe20.configure(text='''If "Yes then please show the previous name documents
in passport office"''')


        
       

        self.Button4 =Button(top)
        self.Button4.place(relx=0.56, rely=0.900, height=49, width=72)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#c0c0c0")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font10)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Clear''')
        self.Button4.configure (command=self.clearr)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.42, rely=0.900, height=49, width=66)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#c0c0c0")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font10)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Save''')
        #self.Button3.configure(command=application2)
        self.Button3.configure(command=self.fun1)
        self.val=val

        self.Button5 =Button(top)
        self.Button5.place(relx=0.28, rely=0.900, height=49, width=72)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#c0c0c0")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font10)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Next''')
        self.Button5.configure(command=application2)


    def fun1(self):
        res=self.var.get()
        if res==1:
            response='Yes'
        elif res==2:
            response='No'
            
        if(fname.get()==""):
                messagebox.showerror("Oops!", "Please enter Applicant Name.")
        elif(surname.get()==""):
                messagebox.showerror("Oops!", "Please enter a Surname.")
        elif(gender.get()==""):
                messagebox.showerror("Oops!", "Please select a Gender.")
        
        elif(birth.get()==""):
                messagebox.showerror("Oops!", "Please enter Date of Birth.")
        else:
        
        #self.conn = db.connect('Sample.db')
        #self.cur = self.conn.cursor()
            cur.execute ('''CREATE TABLE IF NOT EXISTS backup
                (
                 Fname TEXT,
                 Lname TEXT,
                 Gender TEXT,
                 DOB TEXT,
                 rb TEXT
                 )''')

               
            cur.execute("insert into backup values(?,?,?,?,?)",(self.Entry1.get(),self.Entry2.get(),self.TCombobox1.get(),self.Entry3.get(),response))
            cuttr=cur.execute('''SELECT * from backup''')
            for data in cuttr:
                
                print("Name: ",data[0])
                print("Surname: ",data[1])
                print("Gender: ",data[2])
                print("DATE OF BIRTH: ",data[3])
                print("rb: ",data[4],'\n')
               
            #self.cur.close()
            db.commit()
            cur.close()
        
                
    def clearr(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.TCombobox1.delete(0, END)
        self.Entry3.delete(0, END)
        #self.Radiobutton1.delete(0, END)
        #self.Radiobutton2.delete(0, END)
        


class Application_Form2():
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family Calibri -size 16 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font14 = "-family Calibri -size 10 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font10 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1024x705+149+113")
        top.minsize(120, 1)
        top.maxsize(1028, 749)
        top.resizable(1, 1)
        top.title("Application Form")
        top.configure(background="#ffffff")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.156, height=31, width=1024)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Place Of Birth''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.0, rely=0.227, height=31, width=374)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Is your Place of Birth out of India? *''')



        self.var = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.37, rely=0.207, relheight=0.078
                , relwidth=0.098)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.47, rely=0.207, relheight=0.078
                , relwidth=0.098)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        
        

        

        self.Label3 = Label(top)
        self.Label3.place(relx=0.0, rely=0.284, height=31, width=264)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Village or Town or City *''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.0, rely=0.34, height=31, width=174)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Marital Status *''')


        l=["Single","Married","Divorced","Widow/Widower","Separated"]
        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.180, rely=0.336, relheight=0.051
                , relwidth=0.180)
        self.TCombobox1.configure(values=l)
        self.TCombobox1.configure(font=font11)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=marital)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.41, rely=0.326, height=41, width=244)
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Citizenship of India by *''')

        l=["Birth","Descent","Registration/Naturalization"]
        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.66, rely=0.336, relheight=0.051
                , relwidth=0.250)
        self.TCombobox2.configure(values=l)
        self.TCombobox2.configure(font=font11)
        self.TCombobox2.configure(takefocus="")
        self.TCombobox2.configure(textvariable=cindia)


        self.Label6 = Label(top)
        self.Label6.place(relx=0.0, rely=0.397, height=31, width=194)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''PAN (If available)''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.459, rely=0.397, height=31, width=224)
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font9)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Voter ID (If available)''')

        self.Label8 = Label(top)
        self.Label8.place(relx=0.0, rely=0.468, height=31, width=214)
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font9)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Employment Type *''')


        l=["Government","Homemaker","Not Employed","Others","Retired Government Servant","Retired-Private Service","Self Employed","Student"]
        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.22, rely=0.468, relheight=0.051
                , relwidth=0.750)
        self.TCombobox3.configure(values=l)
        self.TCombobox3.configure(font=font11)
        self.TCombobox3.configure(takefocus="")
        self.TCombobox3.configure(textvariable=emp)

        self.Label9 = Label(top)
        self.Label9.place(relx=0.0, rely=0.525, height=31, width=774)
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font=font9)
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Is either of your parent (in case of minor)/ spouse, a government servant? *''')


        l=["Yes","No"]
        self.TCombobox4 = ttk.Combobox(top)
        self.TCombobox4.place(relx=0.75, rely=0.526, relheight=0.051
                , relwidth=0.120)
        self.TCombobox4.configure(values=l)
        self.TCombobox4.configure(font=font11)
        self.TCombobox4.configure(takefocus="")
        self.TCombobox4.configure(textvariable=category)

        self.Label10 = Label(top)
        self.Label10.place(relx=0.0, rely=0.582, height=31, width=284)
        self.Label10.configure(background="#ffffff")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font=font9)
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Educational Qualification *''')


        l=["7th pass or less","Between 8th & 9th","10th pass & above","Graduate & above"]
        self.TCombobox5 = ttk.Combobox(top)
        self.TCombobox5.place(relx=0.27, rely=0.582, relheight=0.051
                , relwidth=0.180)
        self.TCombobox5.configure(values=l)
        self.TCombobox5.configure(font=font11)
        self.TCombobox5.configure(takefocus="")
        self.TCombobox5.configure(textvariable=edu)

     
        self.Label11 = Label(top)
        self.Label11.place(relx=0.459, rely=0.582, height=31, width=424)
        self.Label11.configure(background="#ffffff")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font=font9)
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Are you eligible for Non-ECR category? *''')


        l=["Yes","No"]
        self.TCombobox6 = ttk.Combobox(top)
        self.TCombobox6.place(relx=0.87, rely=0.582, relheight=0.051
                , relwidth=0.120)
        self.TCombobox6.configure(values=l)
        self.TCombobox6.configure(font=font11)
        self.TCombobox6.configure(takefocus="")
        self.TCombobox6.configure(textvariable=gover)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.186, rely=0.397,height=30, relwidth=0.248)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font11)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(readonlybackground="#f0f0f0f0f0f0")
        self.Entry1.configure(relief="groove")
        self.Entry1.configure(textvariable=pan)

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.693, rely=0.397,height=30, relwidth=0.268)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font11)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(relief="groove")
        self.Entry2.configure(textvariable=voter)

        self.Label12 = Label(top)
        self.Label12.place(relx=0.0, rely=0.652, height=31, width=294)
        self.Label12.configure(background="#ffffff")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font=font9)
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''Visible Distinguishing Mark''')

        self.Label13 = Label(top)
        self.Label13.place(relx=0.0, rely=0.723, height=41, width=204)
        self.Label13.configure(background="#ffffff")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font=font9)
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Aadhaar Number *''')

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.293, rely=0.652,height=30, relwidth=0.502)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font11)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(relief="groove")
        self.Entry3.configure(textvariable=mark)

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.215, rely=0.738,height=30, relwidth=0.58)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font11)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(relief="groove")
        self.Entry4.configure(textvariable=adhaar)

        self.Message1 = Message(top)
        self.Message1.place(relx=0.01, rely=0.794, relheight=0.089
                , relwidth=0.781)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(font=font14)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(relief="groove")
        self.Message1.configure(text='''I, the holder of above mentioned Aadhaar Number , hereby give my consent to Passport Seva to obtain my Aadhaar Number, Name and Fingerprint/Iris for authentication with UIDAI. I have no objection using my identity and biometric information for validation with Aadhaar (CIDR) database only for the purpose of authentication. I agree''')
        self.Message1.configure(width=800)

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.313, rely=0.851, relheight=0.021
                , relwidth=0.046)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font=font14)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Yes''')
        #self.Checkbutton1.configure(variable=application2_support.che63)

        '''self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.361, rely=0.851, relheight=0.021
                , relwidth=0.043)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#ffffff")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(font=font14)
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text=No)
        #self.Checkbutton2.configure(variable=application2_support.che64)'''

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.254, rely=0.284,height=30, relwidth=0.658)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font11)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(textvariable=village)
         
        
        self.Button1 = Button(top)
        self.Button1.place(relx=0.381, rely=0.922, height=34, width=57)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Save''')
        #self.Button1.configure(command=application3)
        self.Button1.configure(command=self.fun2)


        self.Button5 =Button(top)
        self.Button5.place(relx=0.25, rely=0.922, height=34, width=67)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font9)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Next''')
        self.Button5.configure(command=application3)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.5, rely=0.922, height=34, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Clear''')
        self.Button2.configure(command=self.clearr)

        
        self.Ashoka = Button(top)
        self.Ashoka.place(relx=0.01, rely=0.014, height=94, width=57)
        self.Ashoka.configure(activebackground="#ececec")
        self.Ashoka.configure(activeforeground="#000000")
        self.Ashoka.configure(background="#d9d9d9")
        self.Ashoka.configure(disabledforeground="#a3a3a3")
        self.Ashoka.configure(foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")
        
        global _img0
        _img0 = PhotoImage(file="app2.png")
        self.Ashoka.configure(image=_img0)
        self.Ashoka.configure(pady="0")

        self.Button4 = Button(top)
        self.Button4.place(relx=0.781, rely=0.014, height=94, width=217)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        
        global _img1
        _img1 = PhotoImage(file="app2 passport.png")
        self.Button4.configure(image=_img1)
        self.Button4.configure(pady="0")


        self.Label14 = Label(top)
        self.Label14.place(relx=0.08, rely=0.024, height=35, width=145)
        self.Label14.configure(background="#ffffff")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font=font10)
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Passport Seva''')

        self.Label15 = Label(top)
        self.Label15.place(relx=0.08, rely=0.07, height=21, width=186)
        self.Label15.configure(background="#ffffff")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Consular, Passport & Visa Division''')

        self.Label16 = Label(top)
        self.Label16.place(relx=0.08, rely=0.093, height=21, width=260)
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Ministry of External Affairs, Government of India''')


    def fun2(self):
        res=self.var.get()
        if res==1:
            response='Yes'
        elif res==2:
            response='No'

        if(village.get()==""):
                messagebox.showerror("Oops!", "Please enter a Village.")
        elif(marital.get()==""):
                messagebox.showerror("Oops!", "Please select Marital Status.")
        elif(cindia.get()==""):
                messagebox.showerror("Oops!", "Please select Citizenship of India.")
        
        
        elif(emp.get()==""):
                messagebox.showerror("Oops!", "Please select Employment Type.")
        elif(gover.get()==""):
                messagebox.showerror("Oops!", "Please select a Government Type.")
        
        elif(edu.get()==""):
                messagebox.showerror("Oops!", "Please select Education Type.")
        elif(category.get()==""):
                messagebox.showerror("Oops!", "Please select Non-ECR Type.")
        elif(adhaar.get()==""):
                messagebox.showerror("Oops!", "Please enter Adhaar Card Number.")
        else:
            #self.conn = db.connect('Sample.db')
            #self.cur = self.conn.cursor()
            cur.execute ('''CREATE TABLE IF NOT EXISTS backup1
                (
                 rb TEXT,
                 village TEXT,
                 martial status TEXT,
                 cindia TEXT,
                 pan TEXT,
                 vote TEXT,
                 emp TEXT,
                 gov TEXT,
                 edu TEXT,
                 category TEXT,
                 mark TEXT,
                 addhar TEXT
                 )''')

               
            cur.execute("insert into backup1 values(?,?,?,?,?,?,?,?,?,?,?,?)",(response,self.Entry5.get(),self.TCombobox1.get(),self.TCombobox2.get(),self.Entry1.get(),self.Entry2.get(),self.TCombobox3.get(),self.TCombobox6.get(),self.TCombobox5.get(),self.TCombobox4.get(),self.Entry3.get(),self.Entry4.get()))
            cuttr=cur.execute('''SELECT * from backup1''')
            for data in cuttr:
                
                print("rb: ",data[0])
                print("village: ",data[1])
                print("ms: ",data[2])
                print("cindia: ",data[3])
                print("pan: ",data[4])
                print("vote: ",data[5])
                print("emp: ",data[6])
                print("gov: ",data[7])
                print("edu: ",data[8])
                print("category: ",data[9])
                print("mark: ",data[10])
                print("addhar: ",data[11],'\n')
               
            #self.cur.close()
            #self.conn.commit()
            #self.conn.close()
            db.commit()
            cur.close()


       
    
    def clearr(self):
        #self.response.delete(0, END)
        self.Entry5.delete(0, END)
        self.TCombobox1.delete(0, END)
        self.TCombobox2.delete(0, END)
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.TCombobox3.delete(0, END)
        self.TCombobox6.delete(0, END)
        self.TCombobox5.delete(0, END)
        self.TCombobox4.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)



class Application_Form3():
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Calibri -size 16 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font10 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1024x705+149+113")
        top.minsize(120, 1)
        top.maxsize(1028, 749)
        top.resizable(1, 1)
        top.title("Applicatio form")
        top.configure(background="#ffffff")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.190, height=31, width=1024)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Family Details (Father/Mother/Legal Guardian details; at least one is mandatory.) *''')

        self.Ashoka = Button(top)
        self.Ashoka.place(relx=0.017, rely=0.022, height=84, width=47)
        self.Ashoka.configure(activebackground="#ececec")
        self.Ashoka.configure(activeforeground="#000000")
        self.Ashoka.configure(background="#ffffff")
        self.Ashoka.configure(disabledforeground="#a3a3a3")
        self.Ashoka.configure(foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")
        
        
        global _img0
        _img0 = PhotoImage(file="app3.png")
        self.Ashoka.configure(image=_img0)
        self.Ashoka.configure(pady="0")
        self.Ashoka.configure(relief="flat")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.781, rely=0.014, height=102, width=220)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        
        global _img1
        _img1 = PhotoImage(file="app3 passport.png")
        self.Button2.configure(image=_img1)
        self.Button2.configure(pady="0")

        self.Label2 = Label(top)
        self.Label2.place(relx=0.0, rely=0.240, height=31, width=884)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Father's Given Name (Given Name means First Name followed by Middle Name (If any))''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.0, rely=0.350, height=31, width=94)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Surname''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.0, rely=0.440, height=35, width=444)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Legal Guardian's Given Name (if applicable)''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.0, rely=0.540, height=35, width=96)
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Surname''')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.0, rely=0.650, height=35, width=895)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Mother's Given Name (Given Name means First Name followed by Middle Name (If any))''')

        self.Label7 = Label(top)
        self.Label7.place(relx=0.0, rely=0.760, height=35, width=96)
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font9)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Surname''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.017, rely=0.290,height=40, relwidth=0.9)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(relief="groove")
        self.Entry1.configure(textvariable=father_name)
        
        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.017, rely=0.390,height=40, relwidth=0.9)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(relief="groove")
        self.Entry2.configure(textvariable=father_surname)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.017, rely=0.490,height=40, relwidth=0.9)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(relief="groove")
        self.Entry3.configure(textvariable=g_name)

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.017, rely=0.590,height=40, relwidth=0.9)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(relief="groove")
        self.Entry4.configure(textvariable=g_surname)

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.017, rely=0.710,height=40, relwidth=0.9)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(relief="groove")
        self.Entry5.configure(textvariable=mother_name)

        self.Entry6 = Entry(top)
        self.Entry6.place(relx=0.017, rely=0.810,height=40, relwidth=0.9)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font10)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(relief="groove")
        self.Entry6.configure(textvariable=mother_surname)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.400, rely=0.900, height=44, width=57)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Save''')
        #self.Button3.configure(command=application4)
        self.Button3.configure(command=self.fun3)


        self.Button5 =Button(top)
        self.Button5.place(relx=0.300, rely=0.900, height=44, width=57)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font9)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Next''')
        self.Button5.configure(command=application4)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.500, rely=0.900, height=44, width=67)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font9)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Clear''')
        self.Button4.configure(command=self.clearr)
        


        self.Label14 = Label(top)
        self.Label14.place(relx=0.08, rely=0.024, height=35, width=145)
        self.Label14.configure(background="#ffffff")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font=font10)
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Passport Seva''')

        self.Label15 = Label(top)
        self.Label15.place(relx=0.08, rely=0.07, height=21, width=186)
        self.Label15.configure(background="#ffffff")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Consular, Passport & Visa Division''')

        self.Label16 = Label(top)
        self.Label16.place(relx=0.08, rely=0.093, height=21, width=260)
        self.Label16.configure(background="#ffffff")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Ministry of External Affairs, Government of India''')

    def fun3(self):
        if(father_name.get()==""):
                messagebox.showerror("Oops!", "Please enter Father's Name.")
        elif(father_surname.get()==""):
                messagebox.showerror("Oops!", "Please enter a Father's Surname.")
        elif(g_name.get()==""):
                messagebox.showerror("Oops!", "Please enter a Guardian's Name.")
        
        elif(g_surname.get()==""):
                messagebox.showerror("Oops!", "Please enter Guardian's Surame.")
        elif(mother_name.get()==""):
                messagebox.showerror("Oops!", "Please enter Mother's Name.")

        elif(mother_surname.get()==""):
                messagebox.showerror("Oops!", "Please enter Mother's Surame.")

        else:
            
        #self.conn = db.connect('Sample.db')
        #self.cur = self.conn.cursor()
            cur.execute ('''CREATE TABLE IF NOT EXISTS app3
                (
                 FATHER TEXT,
                 FSURNAME TEXT,
                 GUARDIAN TEXT,
                 GSURNAME TEXT,
                 MOTHER TEXT,
                 MSURNAME TEXT
                 )''')

               
            cur.execute("insert into app3 values(?,?,?,?,?,?)",(self.Entry1.get(),self.Entry2.get(),self.Entry3.get(),self.Entry4.get(),self.Entry5.get(),self.Entry6.get()))
            cuttr=cur.execute('''SELECT * from app3''')
            for data in cuttr:
                
                print("father: ",data[0])
                print("surname: ",data[1])
                print("guardian: ",data[2])
                print("surname: ",data[3])
                print("mother: ",data[4])
                print("surname: ",data[5],'\n')
              
               
            #self.cur.close()
            #self.conn.commit()
            #self.conn.close()
            db.commit()
            cur.close()

    
    def clearr(self):
 
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry6.delete(0, END)

class Application_Form4():
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Calibri -size 16 -weight normal -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font10 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font20 = "-family Calibri -size 12 -weight normal -slant roman"

        top.geometry("1024x705+146+94")
        top.minsize(120, 1)
        top.maxsize(1028, 749)
        top.resizable(1, 1)
        top.title("Application form")
        top.configure(background="#ffffff")

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.01, rely=0.014, height=84, width=57)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        
        
        global _img0
        _img0 = PhotoImage(file="app4.png")
        self.Button1.configure(image=_img0)
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.771, rely=0.0, height=102, width=220)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        
        global _img1
        _img1 = PhotoImage(file="app4 passport.png")
        self.Button2.configure(image=_img1)
        self.Button2.configure(pady="0")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.156, height=41, width=1024)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Present Residential Address Details (where applicant presently resides)''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.01, rely=0.397, height=35, width=498)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Is the above address your Permanent Address? *''')


        self.var = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.5, rely=0.380, relheight=0.078
                , relwidth=0.098)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.6, rely=0.380, relheight=0.078
                , relwidth=0.098)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.01, rely=0.241, height=35, width=110)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Address *''')

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.117, rely=0.241,height=95,width=850)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font20)
        #self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(relief="groove")
        self.Entry5.configure(textvariable=address)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.0, rely=0.482, height=35, width=1024)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Contact Details *''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.01, rely=0.582, height=35, width=182)
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Mobile Number*''')
       
        
        self.Label6 = Label(top)
        self.Label6.place(relx=0.518, rely=0.582, height=35, width=210)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Telephone Number''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.723, rely=0.582,height=40, relwidth=0.258)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(relief="groove")
        #self.Entry1.configure(textvariable=telephone)
        
        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.127, rely=0.766,height=40, relwidth=0.6)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(relief="groove")
        self.Entry2.configure(textvariable=email)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.195, rely=0.582,height=40, relwidth=0.287)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(relief="groove")
        self.Entry3.configure(text=mobile_num)

        
        self.Label7 = Label(top)
        self.Label7.place(relx=0.01, rely=0.766, height=35, width=100)
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font9)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''E-mail ID''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.4, rely=0.879, height=49, width=66)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Save''')
        #self.Button3.configure(command=application5)
        self.Button3.configure(command=self.fun4)


        self.Button5 =Button(top)
        self.Button5.place(relx=0.3, rely=0.879, height=49, width=66)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font9)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Next''')
        self.Button5.configure(command=application5)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.518, rely=0.879, height=49, width=72)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font9)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Clear''')
        self.Button4.configure(command=self.clearr)
        

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.283, rely=0.681,height=40, relwidth=0.287)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(relief="groove")
        self.Entry4.configure(text=gmobile_num)
        
        self.Label8 = Label(top)
        self.Label8.place(relx=0.01, rely=0.681, height=35, width=269)
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font9)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Guardian Contact Number''')

        self.Label9 = Label(top)
        self.Label9.place(relx=0.078, rely=0.014, height=35, width=145)
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font=font9)
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Passport Seva''')

        
        self.Label20 = Label(top)
        self.Label20.place(relx=0.08, rely=0.055, height=21, width=186)
        self.Label20.configure(background="#ffffff")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''Consular, Passport & Visa Division''')

        self.Label21 = Label(top)
        self.Label21.place(relx=0.08, rely=0.08, height=21, width=260)
        self.Label21.configure(background="#ffffff")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''Ministry of External Affairs, Government of India''')

    

    def fun4(self):
        
        res=self.var.get()
        if res==1:
            response='Yes'
        elif res==2:
            response='No'
            
        if valid_phone(mobile_num.get())==False:
            messagebox.showerror("Oops!", "Please enter a valid Mobile number.")
        elif(mobile_num.get()==""):
                messagebox.showerror("Oops!", "Please enter a Mobile number.")
        elif(gmobile_num.get()==""):
                messagebox.showerror("Oops!", "Please enter Guradian Mobbile number.")
        elif valid_gphone(gmobile_num.get())==False:
            messagebox.showerror("Oops!", "Please enter a valid Guardian Mobile number.")
        elif(email.get()==""):
                messagebox.showerror("Oops!", "Please enter a E-mail ID.")
        elif(address.get()==""):
                messagebox.showerror("Oops!", "Please enter a Address.")
                
            
        else:   
        #self.conn = db.connect('Sample.db')
        #self.cur = self.conn.cursor()
            cur.execute ('''CREATE TABLE IF NOT EXISTS data5
                (
                 ADDRESS TEXT,
                 RB TEXT,
                 MOBILE TEXT,
                 GMOBILE TEXT,
                 TMOBILE TEXT,
                 EMAIL TEXT
                 )''')

               
            cur.execute("insert into data5 values(?,?,?,?,?,?)",(self.Entry5.get(),response,self.Entry3.get(),self.Entry4.get(),self.Entry1.get(),self.Entry2.get()))
            cuttr=cur.execute('''SELECT * from data5''')
            for data in cuttr:
                
                print("address: ",data[0])
                print("rb: ",data[1])
                print("mobile: ",data[2])
                print("gmobile: ",data[3])
                print("tmobile: ",data[4])
                print("email: ",data[5],'\n')
              
               
            #self.cur.close()
            #self.conn.commit()
            #self.conn.close()
            db.commit()
            cur.close()
            
    
        
    def clearr(self):
 
        self.Entry5.delete(0, END)
        #self.response.delete(0,END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)




class Application_Form5():
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font10 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1024x705+119+110")
        top.minsize(120, 1)
        top.maxsize(1028, 749)
        top.resizable(1, 1)
        top.title("Application Form")
        top.configure(background="#ffffff")

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.184, height=35, width=1023)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Passport Details''')

        

        self.Label2 = Label(top)
        self.Label2.place(relx=0.01, rely=0.241, height=35, width=217)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Type of Application *''')

        self.var = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.3, rely=0.238, relheight=0.048
                , relwidth=0.098)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Normal''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.48, rely=0.238, relheight=0.048
                , relwidth=0.098)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''Tatkaal''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.01, rely=0.284, height=35, width=272)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Type of Passport Booklet *''')

        self.var1 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.3, rely=0.278, relheight=0.078
                , relwidth=0.12)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var1)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''36 Pages''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.48, rely=0.278, relheight=0.078
                , relwidth=0.12)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var1)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''60 Pages''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.007, rely=0.397, height=35, width=546)
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''1)Have you ever applied for passport, but not issued? *''')

        self.var2 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.87, rely=0.390, relheight=0.078
                , relwidth=0.06)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var2)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.94, rely=0.390, relheight=0.078
                , relwidth=0.05)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var2)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)


        self.Label5 = Label(top)
        self.Label5.place(relx=0.0, rely=0.34, height=35, width=1023)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Other Details''')

        self.Message1 = Message(top)
        self.Message1.place(relx=0.0, rely=0.451, relheight=0.102
                , relwidth=0.698)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''2) Have you ever been charged with criminal proceedings or any arrest warrant/ summon pending  before a court of India? *''')
        self.Message1.configure(width=710)

        self.var3 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.87, rely=0.446, relheight=0.078
                , relwidth=0.06)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var3)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.94, rely=0.444, relheight=0.078
                , relwidth=0.05)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var3)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Message2 = Message(top)
        self.Message2.place(relx=0.0, rely=0.539, relheight=0.155
                , relwidth=0.808)
        self.Message2.configure(background="#ffffff")
        self.Message2.configure(font=font9)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''3) Have you at any time during the period of 5 years immediately preceding the date of this application  been convicted by a court in India for any criminal offence and sentenced to imprisonment  for  two  years or more? *''')
        self.Message2.configure(width=827)


        self.var4 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.87, rely=0.543, relheight=0.078
                , relwidth=0.06)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var4)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.94, rely=0.543, relheight=0.078
                , relwidth=0.05)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var4)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Message3 = Message(top)
        self.Message3.place(relx=-0.01, rely=0.675, relheight=0.061
                , relwidth=0.537)
        self.Message3.configure(background="#ffffff")
        self.Message3.configure(font=font9)
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''4) Have you ever been refused or denied passport? *''')
        self.Message3.configure(width=550)


        self.var5 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.87, rely=0.660, relheight=0.078
                , relwidth=0.06)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var5)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.94, rely=0.660, relheight=0.078
                , relwidth=0.05)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var5)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Message4 = Message(top)
        self.Message4.place(relx=0, rely=0.723, relheight=0.061
                , relwidth=0.576)
        self.Message4.configure(background="#ffffff")
        self.Message4.configure(font=font9)
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text='''5) Has your Passport ever been impounded or Revoked? *''')
        self.Message4.configure(width=590)

        
        self.var6 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.87, rely=0.71, relheight=0.078
                , relwidth=0.06)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var6)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.94, rely=0.71, relheight=0.078
                , relwidth=0.05)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var6)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)




        self.Message5 = Message(top)
        self.Message5.place(relx=0, rely=0.77, relheight=0.067, relwidth=0.872)

        self.Message5.configure(background="#ffffff")
        self.Message5.configure(font=font9)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(text='''6) Have you ever applied for/ been granted political asylum to/ by any foreign country? *''')
        self.Message5.configure(width=893)


        self.var7 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.87, rely=0.77, relheight=0.078
                , relwidth=0.06)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var7)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.94, rely=0.77, relheight=0.078
                , relwidth=0.05)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var7)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Message6 = Message(top)
        self.Message6.place(relx=0, rely=0.83, relheight=0.092
                , relwidth=0.863)
        self.Message6.configure(background="#ffffff")
        self.Message6.configure(font=font9)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''7) Have you ever returned to India on Emergency Certificate (EC) or were ever deported or repatriated? *''')
        self.Message6.configure(width=884)


        self.var8 = IntVar()
        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.87, rely=0.83, relheight=0.078
                , relwidth=0.06)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffffff")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(variable=self.var8)
        self.Radiobutton1.configure(value=1)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(offrelief="flat")
        self.Radiobutton1.configure(text='''Yes''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)
        

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.94, rely=0.83, relheight=0.078
                , relwidth=0.05)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffffff")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(variable=self.var8)
        self.Radiobutton2.configure(value=2)
        #self.Radiobutton1.configure(justify='left')
        self.Radiobutton2.configure(offrelief="flat")
        self.Radiobutton2.configure(text='''No''')
        #self.Radiobutton1.configure(variable=radiobutton_support.selectedButton)

        self.Label6 = Label(top)
        self.Label6.place(relx=0.078, rely=0.028, height=35, width=145)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Passport Seva''')


        self.Label20 = Label(top)
        self.Label20.place(relx=0.08, rely=0.067, height=21, width=186)
        self.Label20.configure(background="#ffffff")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''Consular, Passport & Visa Division''')

        self.Label21 = Label(top)
        self.Label21.place(relx=0.08, rely=0.090, height=21, width=260)
        self.Label21.configure(background="#ffffff")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''Ministry of External Affairs, Government of India''')
        

        self.Button3 = Button(top)
        self.Button3.place(relx=0.4, rely=0.920, height=49, width=66)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Save''')
        self.Button3.configure(command=self.fun5)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.518, rely=0.920, height=49, width=72)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font9)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Clear''')


        self.Button1 = Button(top)
        self.Button1.place(relx=0.01, rely=0.014, height=97, width=62)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        
        self.Button5 =Button(top)
        self.Button5.place(relx=0.290, rely=0.920, height=49, width=72)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font9)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Next''')
        self.Button5.configure(command=application6)
        
        global _img0
        _img0 = PhotoImage(file="snip.png")
        self.Button1.configure(image=_img0)
        self.Button1.configure(pady="0")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.771, rely=0.014, height=102, width=220)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")

        global _img1
        _img1 = PhotoImage(file="snip passport.png")
        self.Button2.configure(image=_img1)
        self.Button2.configure(pady="0")


    def fun5(self):
        global res
        res=self.var.get()
        if res==1:
            response='Normal'
        elif res==2:
            response='Tatkaal'
            
        res1=self.var1.get()
        if res1==1:
            response1='36 Pages'
        elif res1==2:
            response1='72 Pages'

        res2=self.var2.get()
        if res2==1:
            response2='Yes'
        elif res2==2:
            response2='No'

        res3=self.var3.get()
        if res3==1:
            response3='Yes'
        elif res3==2:
            response3='No'

        res4=self.var4.get()
        if res4==1:
            response4='Yes'
        elif res4==2:
            response2='No'

        res5=self.var5.get()
        if res5==1:
            response5='Yes'
        elif res5==2:
            response5='No'

        res6=self.var6.get()
        if res6==1:
            response6='Yes'
        elif res6==2:
            response6='No'

        res7=self.var7.get()
        if res7==1:
            response7='Yes'
        elif res7==2:
            response7='No'

        res8=self.var8.get()
        if res8==1:
            response8='Yes'
        elif res8==2:
            response8='No'
        
            
        #self.conn = db.connect('Sample.db')
        #self.cur = self.conn.cursor()
        cur.execute ('''CREATE TABLE IF NOT EXISTS data6
            (
             RB0 TEXT,
             RB1 TEXT,
             RB2 TEXT,
             RB3 TEXT,
             RB4 TEXT,
             RB5 TEXT,
             RB6 TEXT,
             RB7 TEXT,
             RB8 TEXT
             )''')

           
        cur.execute("insert into data6 values(?,?,?,?,?,?,?,?,?)",(response,response1,response2,response3,response4,response5,response6,response7,response8))
        cuttr=cur.execute('''SELECT * from data6''')
        
        for data in cuttr:
            
            print("RBO: ",data[0])
            print("RB1: ",data[1])
            print("RB2: ",data[2])
            print("RB3: ",data[3])
            print("RB4: ",data[4])
            print("RB5: ",data[5])
            print("RB6: ",data[6])
            print("RB7: ",data[7])
            print("RB8: ",data[8],'\n')
          
           
        #self.cur.close()
        #self.conn.commit()
        #self.conn.close()
        db.commit()
        cur.close()

   



class Application_Form6():
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family Calibri -size 18 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        #600x450+97+76
        top.geometry("1024x705+119+110")
        top.minsize(120, 1)
        top.maxsize(1366, 768)
        top.resizable(1, 1)
        top.title("Application Form")
        top.configure(background="#ffffff")

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        
        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.170, height=35, width=2000)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Self Declaration''')

        self.Message1 = Message(top)
        self.Message1.place(relx=0.010, rely=0.230, relheight=0.440
                , relwidth=0.98)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(borderwidth="5")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(relief="sunken")
        self.Message1.configure(text='''I owe allegiance to the sovereignty , unity & integrity of India,  and have not voluntarily acquired citizenship or travel document of any other country. I have not lost, surrendered or been deprived of the the citizenship of India and I affirm that the information given by me in this form and the enclosures is true and I solely responsible for its accuracy, and I am liable to be penalized or prosecuted if found otherwise. I am aware that under the Passport Act, 1967 it is a criminal offence to furnish any false information or to suppress any material information with a view to obtaining passport or travel document.''')
        self.Message1.configure(width=1000)

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.099, rely=0.586, relheight=0.082
                , relwidth=0.100)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font=font9)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''I Agree''')
        #self.Checkbutton1.configure(variable=application6_support.che48)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.025, rely=0.680, height=25, width=95)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''NOTE :''')

        self.Message2 = Message(top)
        self.Message2.place(relx=0.11, rely=0.680, relheight=0.250
                , relwidth=0.84)
        self.Message2.configure(background="#ffffff")
        self.Message2.configure(font=font9)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Applicants are required to submit the proof of address of the present address only, irrespective of the date from which he/she has been residing at the given address. However, he/she is required to mention all the places of stay during previous one year (from the date of application filling) in the Passport application form.''')
        self.Message2.configure(width=904)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.025, rely=0.260, height=25, width=176)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Self Declaration :''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.450, rely=0.900, height=49, width=66)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Save''')
        self.Button3.configure(command=self.success)

        self.Label6 = Label(top)
        self.Label6.place(relx=0.078, rely=0.028, height=35, width=145)
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Passport Seva''')


        self.Label20 = Label(top)
        self.Label20.place(relx=0.08, rely=0.067, height=21, width=186)
        self.Label20.configure(background="#ffffff")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#000000")
        self.Label20.configure(text='''Consular, Passport & Visa Division''')

        self.Label21 = Label(top)
        self.Label21.place(relx=0.08, rely=0.090, height=21, width=260)
        self.Label21.configure(background="#ffffff")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''Ministry of External Affairs, Government of India''')
        

        self.Button1 = Button(top)
        self.Button1.place(relx=0.017, rely=0.022, height=97, width=62)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        
        global _img0
        _img0 = PhotoImage(file="app6.png")
        self.Button1.configure(image=_img0)
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="flat")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.77, rely=0.019, height=102, width=220)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        
        global _img1
        _img1 = PhotoImage(file="app6 passport.png")
        self.Button2.configure(image=_img1)
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")

    def success(self):
        messagebox.showinfo("Success!","You have successfully filled the form ")


def doc_required():
    
  
    top = Tk()    
    top.geometry("2000x2000")  
    top.configure(bg='sky blue')
    top.title("Required document")
      
    menubutton = Menubutton(top, text = "DOCUMENTS REQUIRED FOR PASSPORT ", relief = FLAT, bg='white', fg='blue', font=('arial',30,'bold'))  
      
    menubutton.grid()  
      
    menubutton.menu = Menu(menubutton)  
      
    menubutton["menu"]=menubutton.menu  
      
    menubutton.menu.add_checkbutton(label = "1. Photo passbook of running bank account", variable=IntVar(), font=('arial',20))   
    menubutton.menu.add_checkbutton(label = "2. Voter ID card", variable = IntVar(), font=('arial',20))  
    menubutton.menu.add_checkbutton(label = "3. Aadhaar card", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "4. Electricity Bill", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "5. Rent agreement", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "6. Driving license", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "7. PAN card", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "8. Landline or postpaid mobile bill", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "9. Proof of gas connection", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "10. Certificate from employer of reputed companies on letterhead", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "11. Income Tax assessment order", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "12. School leaving certificate", variable = IntVar(), font=('arial',20))
    menubutton.menu.add_checkbutton(label = "13. Birth certificate issued by the Municipal Corporation", variable = IntVar(), font=('arial',20))

    menubutton.pack()  
      
    top.mainloop() 
    


    
def e_form():
    import webbrowser
    webbrowser.open('file:///E:/pass/PassportApplicationForm_Main_English_V3.0.pdf')
def instruction():
    import webbrowser
    webbrowser.open('file:///E:/pass/instruction booklet.pdf')


def feedback():
    master=Tk()
    w=Canvas(master, width=1000, height=1000)
    w.pack()
    value_1=['Application Submission Process ','Documents','Miscellaneous','National Call Centre','Online Appointment','Online Payment','Online Portal','Passport Fee','Passport Status','Police verification','Postal','Processing of Passport','SMS Service']


    def submit():
        mail=entry_2.get()
        number=entry_4.get()
        dob=entry_3.get()
        i='@'
        if i in mail:
            pass
            if number.isnumeric():
                if len(number)==10:
                    pass
                    if len(dob)==10:
                        pass
                    else:
                        messagebox.showerror("Registration","Please Enter Appropriate Date Of Birth")
                
                else:
                    messagebox.showerror("Registration","Enter 10 digit Telephone Number ")
                    entry_4.delete(0,END)
            else:
                messagebox.showerror("Registration","Enter numeric characters in Telephone number")
                entry_4.delete(0,END)
        else:
              messagebox.showerror("Registration","Invalid E-mail Username")
        #fun()
    def clear():
        entry_0.delete(0,END)
        entry_1.delete(0,END)
        entry_2.delete(0,END)
        entry_3.delete(0,END)
        entry_4.delete(0,END)
        entry_5.delete(0,END)
        entry_6.delete(0,END)
        combo_1.set('')

        
    def feed():
        messagebox.showinfo("Success!","Thanks for your Feedback ")

        
    label_1=Label(master,text="REQUEST DETAILS",font=("arial",15,'bold'))
    label_1.place(x=20,y=30)

    label_2=Label(master,text="Request Mode",font=("arial",12))
    label_2.place(x=20,y=70)

    label_100=Label(master,text="*",fg="red",font=("arial",12))
    label_100.place(x=125,y=70)

    label_7=Label(master,text="Online",font=("arial",12))
    label_7.place(x=260,y=70)


    label_3=Label(master,text="File Number",font=("arial",12))
    label_3.place(x=20,y=140)

    entry_0=Entry(master,font=("arial",12))
    entry_0.place(x=260,y=143)

    label_4=Label(master,text="Category",font=("arial",12))
    label_4.place(x=20,y=210)

    label_99=Label(master,text="*",fg="red",font=("arial",12))
    label_99.place(x=90,y=210)

    combo_1=ttk.Combobox(master,font=("arial",10),width=23,value=value_1)
    combo_1.place(x=260,y=213)
    ######
    label_1=Label(master,text="APPLICANT DETAILS",font=("arial",15,'bold'))
    label_1.place(x=20,y=265)

    label_2=Label(master,text="Applicant Name",font=("arial",12))
    label_2.place(x=20,y=320)

    label_98=Label(master,text="*",fg="red",font=("arial",12))
    label_98.place(x=133,y=320)

    entry_1=Entry(master,font=("arial",12))
    entry_1.place(x=260,y=323)

    label_3=Label(master,text="E-Mail",font=("arial",12))
    label_3.place(x=20,y=380)

    label_98=Label(master,text="*",fg="red",font=("arial",12))
    label_98.place(x=70,y=380)

    entry_2=Entry(master,font=("arial",12))
    entry_2.place(x=260,y=383)

    label_4=Label(master,text="Telephone Number",font=("arial",12))
    label_4.place(x=20,y=440)

    label_98=Label(master,text="*",fg="red",font=("arial",12))
    label_98.place(x=156,y=440)

    entry_4=Entry(master,font=("arial",12))
    entry_4.place(x=260,y=443)

    ###

    label_1=Label(master,text="Request Date",font=("arial",12))
    label_1.place(x=550,y=70)

    date= Label(master, text=f"{dt.datetime.now():%a, %b %d %Y}", font=("helvetica",12))
    date.place(x=750,y=70)
              
    label_2=Label(master,text="Request Description",font=("arial",12))
    label_2.place(x=550,y=140)

    label_98=Label(master,text="*",fg="red",font=("arial",12))
    label_98.place(x=696,y=140)

    entry_5=Entry(master,width=27,font=("arial",12))
    entry_5.place(x=750,y=143)

    ###
    label_3=Label(master,text="Date Of Birth",font=("arial",12))
    label_3.place(x=550,y=320)

    label_3a=Label(master,text="(DD/MM/YYYY)",font=("arial",10))
    label_3a.place(x=550,y=340)

    label_98=Label(master,text="*",fg="red",font=("arial",12))
    label_98.place(x=646,y=320)

    entry_3=Entry(master,width=27,font=("arial",12))
    entry_3.place(x=750,y=323)

    label_4=Label(master,text="Current Address",font=("arial",12))
    label_4.place(x=550,y=380)

    label_98=Label(master,text="*",fg="red",font=("arial",12))
    label_98.place(x=667,y=380)

    label_97=Label(master,text="(Fields marked with asterisk (",font=("arial",10))
    label_97.place(x=666,y=10)

    label_96=Label(master,text="*",fg="red",font=("arial",10))
    label_96.place(x=839,y=10)

    label_95=Label(master,text=") are mandatory.)",font=("arial",10))
    label_95.place(x=847,y=10)

    entry_6=Entry(master,font=("arial",12),width=27)
    entry_6.place(x=750,y=383)
    ###
    b1=Button(master,text="Submit",bg="blue4",fg="white",command=submit,font=("arial",10,"bold"),width=10)
    b1.place(x=320,y=630)

    b2=Button(master,text="Clear",bg="blue4",fg="white",command=clear,font=("arial",10,"bold"),width=10)
    b2.place(x=418,y=630)

    b3=Button(master,text="Back",bg="blue4",fg="white",font=("arial",10,"bold"),width=10)
    b3.place(x=516,y=630)







obj = Passport(root)

root.mainloop()
