from tkinter import *
from tkinter import messagebox
import sys
import time

global count
count =0

class App():
    
    #def reset(self):
        #global count
        #count=1
        #self.t.set('00:00:00')
        
    def start(self):
        global count
        count=0
        self.t.set('00:00:00')
        self.timer()
    
   
    def stop(self):
        global count
        count=1
        #messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}",parent=self.root)
        messagebox.showinfo("Congratulations",f"You worked {self.d}hours")

    
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(count==0):
                self.root.after(1000,self.timer)

    def update_clock(self):
            now = time.strftime("%H:%M:%S")
            self.label.configure(text=now)
            self.label.place(x=160,y=200)
            self.root.after(1000, self.update_clock)

            
        
    def __init__(self):
        self.root=Tk()
        self.root.title("Record the timing")
        self.root.geometry("500x500")
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t,font=("Goudy old style",40,"bold"),bg="orange")
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Goudy old style",20,"bold"))
        self.bt2 = Button(self.root,text="Stop",command=self.stop ,font=("Goudy old style",20,"bold"))
        #self.bt3 = Button(self.root,text="Reset",command=self.reset,font=("Arial 12 bold"))
        self.lb.place(x=160,y=10)
        self.bt1.place(x=160,y=100)
        self.bt2.place(x=290,y=100)
        #self.bt3.place(x=370,y=100)
        self.label = Label(self.root,text="",font=("Goudy old style",40,"bold"))
        self.update_clock()
        self.root.mainloop()


    

a=App()        

