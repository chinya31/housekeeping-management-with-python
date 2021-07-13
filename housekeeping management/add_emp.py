import os
from subprocess import call
import re
from tkinter import messagebox

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="mini_project")
cur = db.cursor()

import sys

try:
    from Tkinter import *
    from Tkinter.ttk import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    
def valid():
    l = list()
    name = name_entry.get()
    username = username_entry.get()
    contact = contact_entry.get()
    password = pass_entry.get()
    age = age_entry.get()

    if name=="":
        messagebox.showinfo('Information','Empty name')
    elif username=="":
        messagebox.showinfo('Information','Empty username')
    elif contact=="":
        messagebox.showinfo('Information','Empty contact')
    elif password=="":
        messagebox.showinfo('Information','Empty password')
    elif age=="":
        messagebox.showinfo('Information','Empty age')
    elif len(contact)!=10:
        messagebox.showinfo('Information','Check contact number')
    else:
        l.append(username)
        l.append(name)
        l.append(contact)
        l.append(age)
        l.append(password)
        l.append("yes")

        try:
            sql = "INSERT INTO staff VALUES (%s,%s,%s,%s,%s,%s)"

            cur.execute(sql,l)
            db.commit()

            messagebox.showinfo('Information','Employee added successfully!')
            root.destroy()
        except:
            messagebox.showinfo('Error','Check username')

root = Tk()

root.geometry("250x300+500+110")
root.title("Add Employee")
root.configure(background="#e3edf6")
root.configure(highlightbackground="#3777ac")
root.configure(highlightcolor="black")

#labels
name_label=Label(root,text="Name ")
name_label.configure(bg="#e3edf6")
name_label.configure(pady="15")
name_label.grid(row=0,column=0)

username_label=Label(root,text="Username ")
username_label.configure(bg="#e3edf6")
username_label.configure(pady="15")
username_label.grid(row=1,column=0)

contact_label=Label(root,text="Contact ")
contact_label.configure(bg="#e3edf6")
contact_label.configure(pady="15")
contact_label.grid(row=2,column=0)

pass_label=Label(root,text="Password ")
pass_label.configure(bg="#e3edf6")
pass_label.configure(pady="15")
pass_label.grid(row=3,column=0)

age_label=Label(root,text="Age ")
age_label.configure(bg="#e3edf6")
age_label.configure(pady="15")
age_label.grid(row=4,column=0)


#entry
#global name
#name = StringVar()
name_entry = Entry(root,width=25)
name_entry.place(x=60,y=17,height=22)

username = StringVar()
username_entry = Entry(root,width=25)
username_entry.place(x=60,y=65,height=22)

##contact = StringVar()
contact_entry = Entry(root,width=25)
contact_entry.place(x=60,y=110,height=22)

#password = StringVar()
pass_entry = Entry(root,width=25)
pass_entry.place(x=60,y=160,height=22)

#age = StringVar()
age_entry = Entry(root,width=25)
age_entry.place(x=60,y=210,height=22)

add_btn = Button(root,text="Add")
add_btn.config(command=valid)
add_btn.place(x=90,y=250,width=50,height=25)

root.mainloop()