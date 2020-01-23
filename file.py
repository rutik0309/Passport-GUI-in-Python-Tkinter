from tkinter import *
import sqlite3 
from tkinter import ttk
import webbrowser
import re
from tkinter import messagebox
from datetime import date
root = Tk()



def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def valid_gphone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False


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


with sqlite3.connect("Sample.db") as db:
    cur = db.cursor()
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
    
def application7():
            global app7
            global page9
            app7 = Toplevel()
            page9 = Application_Form7(app7)
            app7.mainloop()     



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

            global var4
            var4=self.TCombobox1.get()               
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

            global var2
            var2=self.Entry1.get()   
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
            global var1
            var1=self.Entry5.get()
               
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
           
            
    
        
    def clearr(self):
 
        self.Entry5.delete(0, END)
        #self.response.delete(0,END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)





    

        
        
class Application_Form5():
    def __init__(self,top=None):
        self.count=1
        self.top=top
        self.var3=IntVar()
        top.configure(height=800,width=900,bg='white')
        top.title("Previous passport")
        
        top.configure(highlightbackground='#ffffff')
        self.label=Label(top,font=('bold',18),text="Previous Passport",width=150,anchor=W,bg='light grey')
        self.label.place(x=0,y=110)

        self.lab=Label(top,font=('bold',18),text="Please Enter Details Of Latest Held/lost/Damaged Passport",bg='light grey',width=110)
        self.lab.place(x=2,y=150)
        self.la=Label(top,font=('bold',18),text='Passport Number',bg='white')
        self.la1=Label(top,font=('bold',18),text='Date of issue(format)dd-mm-yyyy',bg='white')
        self.la2=Label(top,font=('bold',18),text='Place of issue(village/town/city)',bg='white')
        self.lab1=Label(top,font=('bold',18),text='File number',activebackground='#ffffff',bg='white')
        self.lab2=Label(top,font=('bold',18),text='Details of Previous|current official Passport',activebackground='#ffffff',bg='white')        
        self.en1=Entry(top,font=('bold',18))
        self.en2=Entry(top,font=('bold',18))
        self.en3=Entry(top,font=('bold',18))
               
        self.en4=Entry(top,font=('calibre',18))
        
        self.rad5=Radiobutton(top,font=('bold',18),variable=self.var3,value='Details available',text='Other Details available',bg='white')
        self.rad6=Radiobutton(top,font=('bold',18),variable=self.var3,value='Details Unavailable',text='Other Details Unavailable',bg='white')
        self.rad5.place(x=700,y=430)
        self.rad6.place(x=700,y=460)
        self.en1.place(x=700,y=220)
        self.en2.place(x=700,y=270)
        self.en3.place(x=700,y=320)
        
        self.en4.place(x=700,y=370)
 
        self.Button5=Button(top,font=(18),text='Check',command=self.f2)
        self.Button5.place(x=510,y=650)
       

        self.la.place(x=100,y=220)
        self.la1.place(x=100,y=270)
        self.la2.place(x=100,y=320)
        self.lab1.place(x=100,y=370)
        self.lab2.place(x=100,y=430)
        self.Ashoka = Button(top, height=90, width=57,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")

        global _img0
        _img0 = PhotoImage(file="app1.png")
        self.Ashoka.configure(image=_img0)
 
        self.Ashoka.place(x=8,y=10)
        self.Button4 = Button(top)
        self.Button4.place(x=1200,y=0, height=94, width=220)
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

    def f2(self):
            self.count=1+self.count
            self.var3=StringVar()
            count=0
            self.verify1=self.en1.get()
  
            self.verify2=self.en2.get()
            self.verify3=self.en3.get()
      
            self.verify4=self.en4.get()
            count=0
            v1=[2,3,4,5,6]
            v2=[7,8,9]
            if len(self.verify1)==0:
                self.en1.delete(0,END)
                lab44=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field",width=30)
                lab44.place(x=990,y=220)
                count=1
            else:
                if not(re.search('^[A-Z][0-9]+',self.verify1)) or not(len(self.verify1)==8):
                    count==1
                    print(self.verify1)
                    self.en1.delete(0,END)
                    lab44=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid passport number',width=30)
                    lab44.place(x=990,y=220)
                    count=1
                   

            if len(self.verify2)==0:
                self.en1.delete(0,END)
                lab54=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field",width=30)
                lab54.place(x=990,y=270)
                count=1
            else:
                 if re.search('\d{2}-\d{2}-\d{4}',self.verify2):
                     try:
                         div=self.verify2.split('-')
                         print(div)
                         a=date(int(div[2]),int(div[1]),int(div[0]))
                         print(a)
                     except ValueError:
                        print('wrong') 
                        count=1
  
                        self.en3.delete(0,END)
                        lab64=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid date',width=30)
                        lab64.place(x=990,y=270)
                 else:
  
                        self.en3.delete(0,END)
                        lab74=Label(self.top,font=('calibre',12,'bold'),text='Please enter  date in proper format',width=30)
                        lab74.place(x=990,y=270)                      

            if len(self.verify3)==0 :
                self.en3.delete(0,END)
                lab54=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field",width=30)
                lab54.place(x=990,y=320)
                count=1
            else:
                if not(re.search('^[A-z][a-z]+',self.verify3)):
                    count=1
  
                    self.en2.delete(0,END)
                    lab64=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid Place of isuue',width=30)
                    lab64.place(x=990,y=320)
            if len(self.verify4)==0:
                self.en4.delete(0,END)
                lab54=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field",width=30)
                lab54.place(x=990,y=370)
                count=1
            else:
                if not(re.search('[A-Z]{4}[0-9]+',self.verify4))or not(len(self.verify4)==12):
                    count=1
  
                    self.en4.delete(0,END)
                    lab64=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid file number ',width=30)
                    lab64.place(x=990,y=370)
            if self.var3.get()==0:
                    lab94=Label(self.top,font=('calibre',12,'bold'),text='Please select an option ')
                    lab94.place(x=1100,y=430)
            print(self.var3.get())
            if count==0:
                self.val=messagebox.askquestion("Yes/No",'You have entered right information.\nDo you ant to save information',parent=app5)
                if self.val=='yes':
                    self.funn()
                
                 
        
    def funn(self):
      
      
            cur.execute ('''CREATE TABLE IF NOT EXISTS type(


             Pass_no TEXT,
             DOI TEXT,
             Place_issue TEXT,
             File_no TEXT,
             avail TEXT
             )''')

           
        
            cur.execute("insert into type values(?,?,?,?,?)",(self.en1.get(),self.en2.get(),self.en3.get(),self.en4.get(),self.var3.get()))
            cuttr=cur.execute('''SELECT * from type ''')
            for data in cuttr:
                print("details: ",data[0])
                print("Passport Number: ",data[1])
                print("Date of issue: ",data[2])
                print("Place of issue: ",data[3])
                print("file no: ",data[4])
            db.commit()
            global value_var
            value_var=(self.en4.get(),)
                
            messagebox.showinfo('Saved','Data saved\npress ok to continue',parent=app5)
            application6()
            #self.cur.close()
 
       

class Application_Form6():
    
    def __init__(self,top=None):
        
        self.top=top
        self.var3=IntVar()
        top.configure(height=800,width=900,bg='white')
        top.title("Emergency Contact")
        
        
        self.label=Label(top,font=('calibre',18,'bold'),text="Emergency contact",width=150,anchor=W,bg='light grey')
        self.label.place(x=0,y=90)

        self.lab=Label(top,font=('calibre',18,'bold'),text="Name(format)\nFirst Name\tLast Name")
        self.la=Label(top,font=('calibre',18,'bold'),text='Mobile Number')
        self.la1=Label(top,font=('calibre',18,'bold'),text='Telephone Number')
        self.la2=Label(top,font=('calibre',18,'bold'),text='Email-id')
        self.en1=Entry(top,font=('calibre',18,'bold'))
        self.en2=Entry(top,font=('calibre',18,'bold'))
        self.en3=Entry(top,font=('calibre',18,'bold'))
        self.en4=Entry(top,font=('calibre',18,'bold'))
        self.but=Button(top,font=('calibre',18,'bold'),text='check information',command=self.f1,bg='light grey')
    
        self.en1.place(x=700,y=150)
        self.en2.place(x=700,y=230)
        self.en3.place(x=700,y=280)
        self.en4.place(x=700,y=330)
        self.but.place(x=500,y=550)
        self.lab.place(x=100,y=150)

        self.la.place(x=100,y=230)
        self.la1.place(x=100,y=280)
        self.la2.place(x=100,y=330)
        self.Ashoka = Button(top, height=90, width=57,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")

        global _img0
        _img0 = PhotoImage(file="app1.png")
        self.Ashoka.configure(image=_img0)
 
        self.Ashoka.place(x=8,y=0)
        self.Button4 = Button(top)
        self.Button4.place(x=1200,y=0, height=94, width=220)
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




    def f1(self):

            count=0
            self.verify1=self.en1.get()
  
            self.verify2=self.en2.get()
            self.verify3=self.en3.get()
            self.verify4=self.en4.get()
            count=0
            v1=[2,3,4,5,6]
            v2=[7,8,9]
            if len(self.verify1)==0:
                self.en1.delete(0,END)
                lab44=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field")
                lab44.place(x=960,y=150)
                count=1
            else:
                if not(re.search('([a-z]|[A-Z])+\s([a-z]|[A-Z])+',self.verify1)):
                    count==1
                    print(self.verify1)
                    self.en1.delete(0,END)
                    lab44=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid name which contains only alphabets and spaces')
                    lab44.place(x=960,y=150)
                    count=1
                   

            if len(self.verify2)==0:
                self.en1.delete(0,END)
                lab54=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field")
                lab54.place(x=960,y=230)
                count=1
            else:
                if not(re.search('^[7,8,9][0-9]+',self.verify2)) or not(len(self.verify2)==10):
                    count=1
  
                    self.en2.delete(0,END)
                    lab64=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid phone nunmber which\nstarts from 7,8,9 and is of 10 digits')
                    lab64.place(x=960,y=230)
            if len(self.verify3)==0:
                self.en3.delete(0,END)
                lab54=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field")
                lab54.place(x=960,y=280)
                count=1
            else:
                if not(re.search('^[2-6][0-9]+',self.verify3))  or not(len(self.verify3)==8):
                    count=1
  
                    self.en3.delete(0,END)
                    lab64=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid  telephone nunmber which\nstarts from 2 to 6 and is of 8 digits')
                    lab64.place(x=960,y=280)
            if len(self.verify4)==0:
                self.en4.delete(0,END)
                lab54=Label(self.top,font=('calibre',12,'bold'),text="Please complete this field")
                lab54.place(x=960,y=330)
                count=1
            else:
                if not(re.search('^\w+([\.-_]\w+)*@([a-z]|[A-Z])+\.([a-z]|[A-Z])+',self.verify4)):
                    count=1
  
                    self.en4.delete(0,END)
                    lab64=Label(self.top,font=('calibre',12,'bold'),text='Please enter valid email id ')
                    lab64.place(x=960,y=330)   
            if count==0:
                
                self.val=messagebox.askquestion("Yes/No",'You have entered right information.\nDo you ant to save information',parent=app6)
                if self.val=='yes':
                    self.funn2()

    def funn2(self):
    
            
           
            cur.execute ("""CREATE TABLE IF NOT EXISTS emerge(
             Name TEXT,
             Mobil_no TEXT,
             Tele_no TEXT,
             email_ID TEXT
             
             )""")
            global gud
            gud=self.en1.get()
           
        
            cur.execute("insert into emerge values(?,?,?,?)",(self.en1.get(),self.en2.get(),self.en3.get(),self.en4.get()))
            cuttr=cur.execute("SELECT * from emerge ")
            for data in cuttr:
                print("Name\Address: ",data[0])
                print("Mobile number: ",data[1])
                print("Telephone number: ",data[2])
                print("Email id: ",data[3])
            db.commit()
            
            #self.cur.close()

           
            messagebox.showinfo("Saved", "Data Saved Successfully\npress ok to continue",parent=app6)
            application7()
              


class Application_Form7():
    def __init__(self,top=None):
        self.top=top
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        
        top.configure(height=800,width=900,bg='white')
        top.title("Passport Verification Details")
        
        top.configure(highlightbackground='#ffffff')
        self.label=Label(top,font=('bold',18),text="Passport Verification Details",width=150,anchor=W,bg='white')
        self.label.place(x=0,y=800)
        self.lab=Label(top,font=('bold',18),text="Please verify the details below(the spelling of name,addresswhich will be printed on your passport",width=100)
        self.la=Label(top,font=('bold',18),text='REPUBLIC OF INDIA',width=80)
        self.la1=Label(top,font=('bold',18),text='Please produce original documents at the time of submission of form.',width=70)
       
        self.lab1=Label(top,font=('bold',18),text='Applicants photo',activebackground='#ffffff',height=7,width=20,bg='light grey')
        self.lab2=Label(top,font=('bold',18),text='Applicants signature',activebackground='#ffffff',height=2,width=20,bg='light grey')        
       
        self.lab4=Label(top,font=('bold',18),text='Applicants Name',activebackground='#ffffff',bg='white')
        self.lab5=Label(top,font=('bold',18),text='Address',activebackground='#ffffff',bg='white')
        self.lab6=Label(top,font=('bold',18),text="Father's Name",activebackground='#ffffff',bg='white')
        self.lab7=Label(top,font=('bold',18),text="Gender",activebackground='#ffffff',bg='white')
        self.lab8=Label(top,font=('bold',18),text='Date of Issue',activebackground='#ffffff',bg='white')
        self.lab9=Label(top,font=('bold',18),text='Place of Issue',activebackground='#ffffff',bg='white')
        self.lab10=Label(top,font=('bold',18),text='Old Passport No',activebackground='#ffffff',bg='white')
        self.lab11=Label(top,font=('bold',18),text='File Number',activebackground='#ffffff',bg='white')
        
        self.lab43=Label(top,font=('bold',18),activebackground='#ffffff')
        self.lab53=Label(top,font=('bold',18),activebackground='#ffffff')
        self.lab63=Label(top,font=('bold',18),activebackground='#ffffff')
        self.lab73=Label(top,font=('bold',18),activebackground='#ffffff')
        self.lab83=Label(top,font=('bold',18),activebackground='#ffffff')
        self.lab443=Label(top,font=('bold',18),activebackground='#ffffff')
        self.lab543=Label(top,font=('bold',18),activebackground='#ffffff')
        self.lab643=Label(top,font=('bold',18),activebackground='#ffffff')
  
      
        self.lab.place(x=50,y=125)
        self.la.place(x=100,y=170)
        self.la1.place(x=100,y=229)
       
        self.lab1.place(x=100,y=290)
        self.lab2.place(x=100,y=489)        
    
       
        self.lab4.place(x=600,y=340)
        self.lab5.place(x=600,y=390)        
        self.lab6.place(x=600,y=440)
       
        self.lab7.place(x=600,y=490)
        self.lab8.place(x=600,y=540)
        self.lab9.place(x=600,y=590)
        self.lab10.place(x=600,y=640)
        self.lab11.place(x=600,y=690)
   
       
        self.lab43.place(x=800,y=340)
        self.lab53.place(x=800,y=390)        
        self.lab63.place(x=800,y=440)
       
        self.lab73.place(x=800,y=490)
        self.lab83.place(x=800,y=540)
        self.lab443.place(x=800,y=590)
        self.lab543.place(x=800,y=640)        
        self.lab643.place(x=800,y=690)
       
 
        self.Ashoka = Button(top, height=90, width=57,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",foreground="#000000")
        self.Ashoka.configure(highlightbackground="#d9d9d9")
        self.Ashoka.configure(highlightcolor="black")

        global _img0
        _img0 = PhotoImage(file="app1.png")
        self.Ashoka.configure(image=_img0)
 
        self.Ashoka.place(x=8,y=0)
        self.Button4 = Button(top)
        self.Button4.place(x=1200,y=0, height=94, width=220)
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
  
        
        self.comm=Button(top,font=(18),text='Paynow',command=self.paynow)
        self.comm.place(x=305,y=650)

    
        self.lab43.configure(text=gud)
        
        

        cuttr=cur.execute("SELECT * from type where File_no=?",value_var )
        for data in cuttr:
                self.lab543.configure(text=data[0])
                self.lab83.configure(text=data[1])
                self.lab443.configure(text=data[2])
                self.lab643.configure(text=data[3])
 
        self.lab53.configure(text=var1)
  
        self.lab63.configure(text=var2)
      
        self.lab73.configure(text=var4)            

       
        #self.cur.close()
       
        cur.close()

    def paynow(self):
        webbrowser.open("https://onlinesbi.com/")


obj = Application_Form1(root)
root.mainloop()
