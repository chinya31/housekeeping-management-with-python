import os
from subprocess import call
import re
from tkinter import messagebox

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="mini_project")
cur = db.cursor()

import sys

font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

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

def emp_add():
    call(["python", "add_emp.py"])


class emp_performance():
    def __init__(self):
        root = Tk()

        root.geometry("470x240+500+110")
        root.title("Performance Index")
        root.configure(background="#e3edf6")
        root.configure(highlightbackground="#3777ac")
        root.configure(highlightcolor="black")

        tree = ttk.Treeview(root,columns=("1","2","3"),height=10)

        tree.column("1",width=150,anchor=CENTER)
        tree.column("2",width=150,anchor=CENTER)
        tree.column("3",width=150,anchor=CENTER)
        #tree.column("4",width=100)

        tree.heading("1",text="Room No")
        tree.heading("2",text="Staff Assigned")
        tree.heading("3",text="Rating")
        #tree.heading("4",text="Age")
        tree['show'] = 'headings'

        #tree.insert('','end',values=("john","4"))
        #tree.insert('','end',values=("jenny","6"))
        #tree.insert('','end',values=("robert","7"))
        #tree.config(font=font14)

        cur.execute("select * from rating")
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", END, values=row)

        tree.pack()


class emp_list():
    def __init__(self):
        root = Tk()

        root.geometry("480x400+500+110")
        root.title("Manage Employees")
        root.configure(background="#e3edf6")
        root.configure(highlightbackground="#3777ac")
        root.configure(highlightcolor="black")

        tree = ttk.Treeview(root,columns=("1","2","3","4"),height=17)
        #tree["columns"] = ("1","2","3","4")

        tree.column("1",width=100,anchor=CENTER)
        tree.column("2",width=100,anchor=CENTER)
        tree.column("3",width=100,anchor=CENTER)
        tree.column("4",width=100,anchor=CENTER)

        tree.heading("1",text="Name")
        tree.heading("2",text="Username")
        tree.heading("3",text="Contact")
        tree.heading("4",text="Age")
        tree['show'] = 'headings'

        #tree.insert('','end',values=("john","john45","1265478930","32"))
        #tree.insert('','end',values=("jenny","jenny6","8597463217","29"))
        #tree.insert('','end',values=("robert","12robert","9874563210","46"))

        cur.execute("select name,username,contact,age from staff")

        rows = cur.fetchall()

        for row in rows:
            tree.insert("", END, values=row)

        tree.pack()

class start():
    def __init__(self):
        root = Tk()

        root.geometry("450x350+500+110")
        root.title("Manage Employees")
        root.configure(background="#e3edf6")
        root.configure(highlightbackground="#3777ac")
        root.configure(highlightcolor="black")

            
         # add employee button widget
        b0 = Button(root,text="Add Employee")
        b0.configure(relief=RAISED)
        b0.configure(activebackground="#3777ac")
        b0.configure(height=2, width=25)
        b0.configure(highlightcolor="black")
        b0.configure(command=emp_add)
        b0.configure(pady="5")
        b0.place(x=130,y=50)

        # list button widget
        b1 = Button(root,text="List of Employees")
        b1.configure(relief=RAISED)
        b1.configure(activebackground="#3777ac")
        b1.configure(height=2, width=25)
        b1.configure(highlightcolor="black")
        b1.configure(command=emp_list)
        b1.configure(pady="5")
        b1.place(x=130,y=100)

        # performance button widget
        b2 = Button(root,text="Performance Index")
        b2.configure(command=emp_performance)
        b2.configure(relief=RAISED)
        b2.configure(height=2, width=25)
        b2.configure(activebackground="#3777ac")
        b2.configure(highlightcolor="black")
        b2.configure(pady="5")
        b2.place(x=130,y=150)

        # back button widget
        b3 = Button(root,text="Back")
        b3.configure(command=root.destroy)
        b3.configure(relief=RAISED)
        b3.configure(height=2, width=25)
        b3.configure(activebackground="#3777ac")
        b3.configure(highlightcolor="black")
        b2.configure(pady="5")
        b3.place(x=130,y=200)

        root.mainloop()


if __name__ == '__main__':
    a=start()