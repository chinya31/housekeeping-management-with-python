from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import os
from subprocess import call

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="mini_project")
cur = db.cursor()

import sys

def click_manage_emp():
    call(["python", "emp_manage.py"])

def click_notice():
    call(["python", "notice.py"])

def house_log():
    root = Tk()

    root.geometry("610x240+500+110")
    root.title("Housekeeping Logs")
    root.configure(background="#e3edf6")
    root.configure(highlightbackground="#3777ac")
    root.configure(highlightcolor="black")

    tree = ttk.Treeview(root,columns=("1","2","3"),height=10)

    tree.column("1",width=200,anchor=CENTER)
    tree.column("2",width=200,anchor=CENTER)
    tree.column("3",width=200,anchor=CENTER)
    #tree.column("4",width=100)

    tree.heading("1",text="Room No")
    tree.heading("2",text="In-charge")
    tree.heading("3",text="Status")
    #tree.heading("4",text="Age")
    tree['show'] = 'headings'

    #tree.insert('','end',values=("102","dirty","jenny"))
    #tree.insert('','end',values=("203","clean","john"))
    #tree.insert('','end',values=("101","clean","john"))
    #tree.config(font=font14)
    
    cur.execute("select roomno,name,status from todo")
    rows = cur.fetchall()

    for row in rows:
        tree.insert("", END, values=row)

    tree.pack()

root = Tk()

root.geometry("600x350+500+110")
root.title("Admin Window")
root.configure(background="#e3edf6")
root.configure(highlightbackground="#3777ac")
root.configure(highlightcolor="black")

Frame_login = Frame(root,bg="DeepSkyBlue2")
Frame_login.place(x=400,y=0,height=400,width=180)

b1=Button(root,text="Manage Employees",height=2,width=30)
b1.configure(relief=RAISED,activebackground="DeepSkyBlue2",command=click_manage_emp)
b1.place(x=50,y=90)

b2=Button(root,text="Housekeeping Logs",height=2,width=30)
b2.configure(relief=RAISED,activebackground="DeepSkyBlue2",command=house_log)
b2.place(x=50,y=140)

b3=Button(root,text="Notice Board",height=2,width=30)
b3.configure(relief=RAISED,activebackground="DeepSkyBlue2",command=click_notice)
b3.place(x=50,y=190)

b4=Button(root,text="Logout",height=2,width=30)
b4.configure(relief=RAISED,activebackground="DeepSkyBlue2",command=root.destroy)
b4.place(x=50,y=240)

image= Image.open("coach.png")
resized = image.resize((150, 150), Image.ANTIALIAS)
pic=ImageTk.PhotoImage(resized)
l1=Label(root,image=pic,background="DeepSkyBlue2")
l1.place(x=413,y=50)

l2=Label(root,text="ADMIN",font=("Helvetica", 22),foreground="navy",background="DeepSkyBlue2")
l2.place(x=450,y=220) 
root.mainloop()
