from tkinter import *
from PIL import Image, ImageTk
import sys
from tkinter import messagebox
import time
import tkinter.ttk as ttk
from subprocess import call

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="mini_project")
cur = db.cursor()

font16 = "-family {Swis721 BlkCn BT} -size 16 -weight bold "  \
    "-slant roman -underline 0 -overstrike 0"

def click_timer():
        call(["python", "time.py"])


def rating():
        root = Tk()

        root.geometry("470x240+500+110")
        root.title("Performance")
        root.configure(background="#e3edf6")
        root.configure(highlightbackground="#3777ac")
        root.configure(highlightcolor="black")

        tree = ttk.Treeview(root,columns=("1","2"),height=10)

        tree.column("1",width=150,anchor=CENTER)
        tree.column("2",width=300,anchor=CENTER)
        #tree.column("3",width=100)
        #tree.column("4",width=100)

        tree.heading("1",text="Room No")
        tree.heading("2",text="Rating Given")
        #tree.heading("3",text="Contact")
        #tree.heading("4",text="Age")
        tree['show'] = 'headings'

        #tree.insert('','end',values=("101","4"))
        #tree.insert('','end',values=("204","5"))
        #tree.insert('','end',values=("403","4"))
        #tree.config(font=font14)

        sql = "SELECT name FROM staff WHERE username=%s"
        l = list()
        global uname
        l.append(uname)
        #print(l)

        cur.execute(sql,l)
        user = cur.fetchall()
        user = str(user)
        n = ""
        for char in user:
            if ord(char) >= 65 and ord(char) <= 90:
                n += char
            elif ord(char) >= 97 and ord(char) <= 122:
                n += char
        #print(n)

        sql = "select roomno,rate from rating where name=%s"
        l.clear()
        l.append(n)

        cur.execute(sql,l)
        rows = cur.fetchall()

        for row in rows:
                tree.insert("", END, values=row)

        tree.pack()


def click_done():
        ##print("done")
        global n
        cur.execute("update todo set status='done' where name=%s",(n,))
        cur.execute("update staff set avaliable='yes' where name=%s",(n,))
        db.commit()
        messagebox.showinfo("Info","Nice work")
        global to_do
        to_do.destroy()

def to_do():

        global to_do
        to_do = Tk()

        to_do.geometry("770x240+500+110")
        to_do.title("To-Do List")
        to_do.configure(background="#e3edf6")
        to_do.configure(highlightbackground="#3777ac")
        to_do.configure(highlightcolor="black")

        tree = ttk.Treeview(to_do,columns=("1","2","3"),height=6)

        tree.column("1",width=150,anchor=CENTER)
        tree.column("2",width=300,anchor=CENTER)
        tree.column("3",width=300,anchor=CENTER)
        #tree.column("4",width=100)

        tree.heading("1",text="Room No")
        tree.heading("2",text="To-Do ")
        tree.heading("3",text="Extra Request")
        #tree.heading("4",text="Age")
        tree['show'] = 'headings'

        #tree.insert('','end',values=("101","Make bed, Mop floor"))
        #tree.insert('','end',values=("204","Laundry"))
        #tree.insert('','end',values=("403","Clean room, Clean Bathroom"))
        #tree.config(font=font14)

        tree.pack()

        done_btn = Button(to_do,text="Done",font=font16,command=click_done,state=NORMAL)
        done_btn.pack()
        
        sql = "SELECT name FROM staff WHERE username=%s"
        l = list()
        global uname
        l.append(uname)
        #print(l)

        cur.execute(sql,l)
        user = cur.fetchall()
        user = str(user)
        global n
        n = ""
        for char in user:
            if ord(char) >= 65 and ord(char) <= 90:
                n += char
            elif ord(char) >= 97 and ord(char) <= 122:
                n += char
        #print(n)

        l.clear()
        l.append(n)

        sql = "select roomno,tasks,extra_req from todo where name=%s and status='in progress'"

        cur.execute(sql,l)
        rows = cur.fetchall()

        if len(rows)==0:
                done_btn['state'] = DISABLED

        for row in rows:
                tree.insert("", END, values=row)
        
        

def notice_click():
        notice_window = Tk()

        cur.execute("select notice from note")
        note_s = cur.fetchone()
        if note_s[0]==None:
                note = ""
        else:
                note = note_s[0]

        #note = "You will see notice here"

        notice_window.geometry("450x350+500+110")
        notice_window.title("Notice Board")
        notice_window.configure(background="#e3edf6")
        notice_window.configure(highlightbackground="#3777ac")
        notice_window.configure(highlightcolor="black")

        # text field
        notice = Text(notice_window,background="white",pady="15",font=font16,height=8,width=30)
        notice.insert(INSERT,note)
        notice.config(state=DISABLED)
        notice.place(x=40,y=20) 


        # back button widget
        b3 = Button(notice_window,text="Back")
        b3.configure(command=notice_window.destroy)
        b3.configure(relief=RAISED)
        b3.configure(height=2, width=10)
        b3.configure(activebackground="#3777ac")
        b3.configure(highlightcolor="black")
        b3.configure(pady="5")
        b3.place(x=170,y=270)


def change_status(sta):
        global status_button
        if sta=="yes":
                cur.execute("update staff set avaliable='no' where username=%s",(uname,))
                status_button.config(bg="red",text="Not Avaliable")
        else:
              cur.execute("update staff set avaliable='yes' where username=%s",(uname,))
              status_button.config(bg="green",text="Avaliable")  
        db.commit()
        return


def start():
        global count
        count =0

        self_root = Tk()
        self_root.geometry("1000x600")
        self_root.title("WELCOME")

        Frame_login = Frame(self_root,bg="white")
        Frame_login.place(x=0,y=0,height=1000,width=1000)
        title = Label(Frame_login,text="STAFF WINDOW",font=("Impact",30,"bold"),fg="orange",bg="white").place(x=250,y=20)

        image = Image.open("worker.png")
        photo = ImageTk.PhotoImage(image)
        varun_label = Label(image=photo)
        varun_label.place(x=650,y=50)

        status_label = Label(self_root, text = 'Change Status', font=('Times new roman',20,'bold'),fg="black",bg="orange").place(x=650,y=400)
        #name_entry = Entry(self_root,textvariable = txt_user, font=('calibre',20,'normal'))

        Todo_btn = Button(self_root,cursor="hand2",text="TO DO LIST",fg="white",bg="black",font=("Times new roman",20),command=to_do).place(x=290,y=200,width=200,height=50)
        Myperform_btn = Button(self_root,cursor="hand2",text="MY PERFORMANCE",fg="white",bg="black",font=("Times new roman",20),command=rating).place(x=250,y=300,width=280,height=50)
        Notice_btn = Button(self_root,cursor="hand2",text="NOTICE BOARD",fg="white",bg="black",font=("Times new roman",20),command=notice_click).place(x=270,y=400,width=250,height=50)
        Logout_btn = Button(self_root,cursor="hand2",text="LOGOUT",fg="white",bg="black",font=("Times new roman",20),command = self_root.destroy).place(x=320,y=500,width=150,height=50)

        #record_button  = Button(self_root,cursor="hand2",text="RECORD THE TIMING",fg="white",bg="black",font=("Times new roman",20),command = click_timer).place(x=650,y=500,width=280,height=60)
                                                                                                                                #command = lambda:[login_function()
        global status_button
        status_button  = Button(self_root,cursor="hand2",text="Status",state=NORMAL,fg="white",font=("Times new roman",20),command=lambda:change_status(st))                                                                                                                        
        status_button.place(x=650,y=450,width=200,height=60)

        cur.execute("select avaliable from staff where username=%s",(uname,))
        st = cur.fetchone()
        st = st[0]
        ##print(st[0])
        if st=="yes":
                status_button.config(bg="green",text="Avaliable")
        else:
                status_button.config(bg="red",text="Not Avaliable")
        #status_button.config(text=st)

        sql = "SELECT name FROM staff WHERE username=%s"
        #l = list()
        #global uname
        #l.append(uname)
        ##print(l)

        cur.execute(sql,(uname,))
        user = cur.fetchall()
        user = str(user)
        global n
        n = ""
        for char in user:
            if ord(char) >= 65 and ord(char) <= 90:
                n += char
            elif ord(char) >= 97 and ord(char) <= 122:
                n += char
        #print(n)

        cur.execute("select * from todo where name=%s",(n,))
        s = list(cur.fetchall())
        #print(s)
        for i in s:
                if "in progress" in i:
                        #global status_button
                        status_button['state'] = DISABLED
                        #print("yes")

        self_root.mainloop()



def login_function():

        

            global uname
            uname = str(txt_user.get())
            #print(uname)

            cur.execute("select * from staff where username=%s and password=%s",(txt_user.get(),txt_pass.get()))
            row = cur.fetchone()

            if txt_pass.get()=="" or txt_user.get()=="":
                messagebox.showerror("Error","All feilds are required",parent = root)
                txt_user.delete(0,"end")
                txt_pass.delete(0,"end")

            elif row==None:
                messagebox.showerror("Error","Inavlid username or password")
                txt_user.delete(0,"end")
                txt_pass.delete(0,"end")
                #messagebox.showerror("Welcome",f"Welcome {txt_user.get()}")
                #secondpage()
            else:
                messagebox.showinfo("Welcome",f"Welcome {txt_user.get()}")
                root.destroy()
                start()
                #messagebox.showinfo("Error","Invalid password")
                #txt_user.delete(0,"end")
                #txt_pass.delete(0,"end")
                          
                

#def __init__(self,root):
root = Tk()
root.title("Staff Login")
root.geometry("800x550")
        

#=====creating frame on root window====#
#=====Login Frame=====
Frame_login = Frame(root,bg="white")
Frame_login.place(x=115,y=50,height=400,width=550)
title = Label(Frame_login,text="Staff LOGIN",font=("Impact",35,"bold"),fg="orange",bg="white").place(x=100,y=10)
desc =  Label(Frame_login,text="Staff user information",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
lbl_user = Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
txt_user = Entry(Frame_login,font=("Times new roman",15),bg="lightgray")
txt_user.place(x=90,y=170,width=350,height=35)
        
lbl_pass = Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
txt_pass = Entry(Frame_login,font=("Times new roman",15),bg="lightgray")
txt_pass.place(x=90,y=240,width=350,height=35)
        
        
Login_btn = Button(root,text="LOGIN",fg="white",bg="orange",font=("Times new roman",20),command = login_function).place(x=300,y=470,width=180,height=40)                                                                                                                           
    
        

#main = Mainwindow(root) #calling function
root.mainloop()