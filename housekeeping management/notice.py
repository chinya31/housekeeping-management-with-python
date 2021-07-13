import os
from subprocess import call
from tkinter import messagebox

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

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="mini_project")
cur = db.cursor(buffered=True)



font16 = "-family {Swis721 BlkCn BT} -size 16 -weight bold "  \
    "-slant roman -underline 0 -overstrike 0"

def click_delete():
    global notice
    notice.delete("1.0","end")

def click_add():

    n = notice.get("1.0","end-1c")
    l = list()
    l.append(n)
    if len(n)==0:
        messagebox.showinfo('Information','Enter something')
    else:
        #print(n)
        sql = "update note set notice=%s where id=1"
        cur.execute(sql,l)
        db.commit()

        global notice_window
        notice_window.quit()
        messagebox.showinfo('Information','Notice uploaded successfully!')


global notice_window
notice_window = Tk()

notice_window.geometry("450x350+500+110")
notice_window.title("Notice Board")
notice_window.configure(background="#e3edf6")
notice_window.configure(highlightbackground="#3777ac")
notice_window.configure(highlightcolor="black")

cur.execute("select notice from note")
note_s = cur.fetchone()
if note_s[0]==None:
    note_s = ""
else:
    note_s = note_s[0]

# text field
notice = Text(notice_window,background="white",pady="15",font=font16,height=8,width=30)
notice.insert('0.0',str(note_s))
notice.place(x=40,y=20) 

# add button widget
b1 = Button(notice_window,text="Add")
b1.configure(relief=RAISED)
b1.configure(activebackground="#3777ac")
b1.configure(height=2, width=10)
b1.configure(highlightcolor="black")
b1.configure(command=click_add)
b1.configure(pady="5")
b1.place(x=20,y=270)

# delete button widget
b2 = Button(notice_window,text="Delete")
b2.configure(command=click_delete)
b2.configure(relief=RAISED)
b2.configure(height=2, width=10)
b2.configure(activebackground="#3777ac")
b2.configure(highlightcolor="black")
b2.configure(pady="5")
b2.place(x=185,y=270)

# back button widget
b3 = Button(notice_window,text="Back")
b3.configure(command=notice_window.destroy)
b3.configure(relief=RAISED)
b3.configure(height=2, width=10)
b3.configure(activebackground="#3777ac")
b3.configure(highlightcolor="black")
b3.configure(pady="5")
b3.place(x=350,y=270)


notice_window.mainloop()