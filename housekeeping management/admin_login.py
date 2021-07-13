from tkinter import *


from tkinter import messagebox
from subprocess import call

def click_admin_window():
    call(["python", "admin_window.py"])

root=Tk()

root.geometry("380x200+500+110")
root.title("Admin Login")
root.configure(background="#e3edf6")
root.configure(highlightbackground="#3777ac")
root.configure(highlightcolor="black")

def on_click(event):
 e.configure(state=NORMAL)
 e.delete(0,END)

def click(event):
 e2.configure(state=NORMAL,show='*')
 e2.delete(0,END)

def submit():
  if e.get()== 'admin1'and e2.get()=='1234' or e.get()=='admin' and e2.get()=='1234':
    root.destroy()
    click_admin_window()
  else:
   messagebox.askretrycancel("Invalid Response","Incorrect Username or Password.\nPlease Try again.") 

e=Entry(root,width=20)
e.place(x=80,y=20)
e.insert(0,"User ID")
e.configure(state=DISABLED)
e.bind("<Button-1>", on_click)


e2=Entry(root,width=20)
e2.place(x=80,y=60)
e2.insert(0,"Password")
e2.configure(state=DISABLED)
e2.bind("<Button-1>", click)


b1=Button(root,text="Submit",width=8,command = submit)
b1.place(x=80,y=100)


b2=Button(root,text="Exit",width=8 ,command = quit)
b2.place(x=195,y=100)



root.mainloop()
