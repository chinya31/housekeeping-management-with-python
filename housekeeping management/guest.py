from tkinter import messagebox
import re
import random

import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="mini_project")
cur = db.cursor(buffered=True)

w_set = set()

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


class check_click():
    def __init__(self,op):
        op_list = ["Make Bed","Change Bedding","Extra Bed","Extra Blankets","Clear Dustbin",
                    "Mop Floor","Clean Room","Clean Bathroom","Replenish Bathroom Supplies",
                    "Extra Towels","Laundry"]

        if op_list[op-1] in w_set:
            w_set.remove(op_list[op-1])
            
        else:
            w_set.add(op_list[op-1])
            

class click_submit():
    def __init__(self): 
        global req_entry
        req = req_entry.get()
        #print(req)
        #print(w_set)
        global chores_win
        chores_win.destroy()

        l = list(w_set)
        st = ",".join(l)
        st1 = "in progress"
        #for i in l:
            #st = i.split(",")
        global room
        roomno = room.get()

        cur.execute("select name from staff where avaliable='yes'")
        names = cur.fetchall()
        name = random.sample(names,1)[0]
        #print(name)

        name = str(name)
        h = ""

        for char in name:
            if ord(char) >= 65 and ord(char) <= 90:
                h += char
            elif ord(char) >= 97 and ord(char) <= 122:
                h += char
        #print(h)

        l1 = list()
        l1.append(roomno)
        l1.append(h)
        l1.append(st)
        l1.append(req)
        l1.append(st1)

        #print(l1)

        sql = "INSERT INTO todo VALUES (%s,%s,%s,%s,%s)"

        cur.execute(sql,l1)
        db.commit()

        l.clear()
        l.append(h)

        sql = "UPDATE staff SET avaliable = 'no' WHERE name = %s"
        cur.execute(sql,l)
        db.commit()

        messagebox.showinfo('Information','Updated successfully!')



class chores():
    def __init__(self):
        
        global chores_win
        chores_win = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font15 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font10 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font20 = "-family {Segoe UI} -size 20 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font28 = "-family {Segoe UI} -size 28 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        chores_win.geometry("750x700+540+110")
        chores_win.title("CHORES")
        chores_win.configure(background="#d9d9d9")
        chores_win.configure(highlightbackground="#d9d9d9")
        chores_win.configure(highlightcolor="black")



        self.Frame1 = Frame(chores_win)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)


        self.Message6 = Label(self.Frame1,text="Please select the services you require")
        self.Message6.pack(side=TOP,fill=X)
        self.Message6.configure(font=font28)


        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.08, rely=0.1, relheight=0.55, relwidth=0.84)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=600)


        bt1 = Checkbutton(self.Frame2,text="Make Bed",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(1)).place(x=30,y=10)
        bt2 = Checkbutton(self.Frame2,text="Change Bedding",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(2)).place(x=30,y=70)
        bt3 = Checkbutton(self.Frame2,text="Extra Bed",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(3)).place(x=30,y=130)
        bt4 = Checkbutton(self.Frame2,text="Extra Blankets",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(4)).place(x=30,y=190)
        bt5 = Checkbutton(self.Frame2,text="Clear Dustbin",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(5)).place(x=30,y=250)
        bt6 = Checkbutton(self.Frame2,text="Mop Floor",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(6)).place(x=30,y=310)
        bt7 = Checkbutton(self.Frame2,text="Clean Room",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(7)).place(x=230,y=10)
        bt8 = Checkbutton(self.Frame2,text="Clean Bathroom",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(8)).place(x=230,y=70)
        bt9 = Checkbutton(self.Frame2,text="Replenish Bathroom Supplies",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(9)).place(x=230,y=130)
        bt10 = Checkbutton(self.Frame2,text="Extra Towels",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(10)).place(x=230,y=190)
        bt11 = Checkbutton(self.Frame2,text="Laundry",onvalue=1,offvalue=0,font=font10,command=lambda:check_click(11)).place(x=230,y=250)

        
        self.request_lbl = Label(self.Frame1,text="Special Request : ")
        self.request_lbl.pack(side=TOP,fill=X)
        self.request_lbl.place(x=56,y=435)
        self.request_lbl.configure(font=font20)


        global req_entry
        req_entry = Entry(self.Frame1)
        req_entry.place(x=300,y=435,width=357,height=50)
        req_entry.configure(font=font15)


        submit = Button(self.Frame1,text="Submit",command=click_submit)
        submit.place(relx=0.08, rely=0.78, relheight=0.09, relwidth=0.24)
        submit.configure(font=font28)

        exitbtn = Button(self.Frame1,text="Exit",command=chores_win.destroy)
        exitbtn.place(relx=0.66, rely=0.78, relheight=0.09, relwidth=0.24)
        exitbtn.configure(font=font28)

class rate():
    
    def __init__(self):
        
        root = Tk()
        root.geometry("400x150+500+110")
        root.title("Rate your Housekeeper")
        root.configure(background="#e3edf6")
        root.configure(highlightbackground="#3777ac")
        root.configure(highlightcolor="black")

        name = StringVar(root)
        name.set("--Name--")

        cur.execute("select name from staff")
        names = cur.fetchall()
        #print(names)

        #dropdown
        #na_str = StringVar()
        d1 = OptionMenu(root,name,*names)
        #d2.set("Maid Name")
        d1.grid(row=1,column=0)

        rate = StringVar(root)
        rate.set("--Rate--")
        #dropdown
        d2= OptionMenu(root,rate,"1","2","3","4","5")
        d2.grid(row=1,column=1)

        label=Label(root,text="  Additional comments :")
        label.configure(bg="#e3edf6")
        label.configure(pady="15")
        label.grid(row=4,column=0)

        s = Entry(root)
        s.grid(row=4,column=1)
        s.get()

        def sub_rate():
            na = list()
            global room
            roomno = room.get()
            na.append(roomno)

            h = str(name.get())
            h1 = ""

            for char in h:
                if ord(char) >= 65 and ord(char) <= 90:
                    h1 += char
                elif ord(char) >= 97 and ord(char) <= 122:
                    h1 += char

            na.append(h1)
            na.append(rate.get())
            na.append(s.get())

            #na = na[0]
            #print(na)

            sql = "INSERT INTO rating VALUES (%s,%s,%s,%s)"

            cur.execute(sql,na)
            db.commit()
            messagebox.showinfo("Successful","Thankyou for your feedback.\nYour response has been successfully recorded.") 
        
        
        b1=Button(root, text ="Submit")
        b1.configure(command=sub_rate)
        b1.configure(relief=RAISED)
        b1.configure(height=1, width=10)
        b1.configure(activebackground="#3777ac")
        b1.configure(highlightcolor="black")
        b1.grid(row=5,column=0)

        b2=Button(root,text="Exit")
        b2.configure(command=root.destroy)
        b2.configure(relief=RAISED)
        b2.configure(height=1, width=10)
        b2.configure(activebackground="#3777ac")
        b2.configure(highlightcolor="black")
        b2.grid(row=5,column=1)
        #root.mainloop()

class menu():

    def __init__(self):

        global room_no_win
        room_no_win.destroy()
        global room
        
        roomno = room.get()
        #print(roomno)

        root = Tk()

        root.geometry("450x350+500+110")
        root.title("Guest Room")
        root.configure(background="#e3edf6")
        root.configure(highlightbackground="#3777ac")
        root.configure(highlightcolor="black")

            
        # labels
        l1 = Label(root,text = "Room No. :",background="#e3edf6",pady="15")
        l1.pack(anchor="nw")
        l2 = Label(root,text = roomno,background="#e3edf6",pady="15")
        l2.place(x=75,y=2)
        l3 = Label(root,text= "Room Type:",background="#e3edf6")
        l3.pack(anchor="nw")
        global typee
        l4 = Label(root,text=typee,background="#e3edf6", pady="13")
        l4.place(x=75,y=38)

        # housekeeping button widget
        b1 = Button(root,text="Housekeeping Services")
        b1.configure(relief=RAISED)
        b1.configure(activebackground="#3777ac")
        b1.configure(height=2, width=25)
        b1.configure(highlightcolor="black")
        b1.configure(command=chores)
        b1.configure(pady="5")
        b1.pack(anchor="s")

        # housekeeper rating button widget
        b2 = Button(root,text="Rate your Housekeeper")
        b2.configure(command=rate)
        b2.configure(relief=RAISED)
        b2.configure(height=2, width=25)
        b2.configure(activebackground="#3777ac")
        b2.configure(highlightcolor="black")
        b2.configure(pady="5")
        b2.pack(anchor="s")

        # exit button widget
        b3 = Button(root,text="Exit")
        b3.configure(command=quit)
        b3.configure(relief=RAISED)
        b3.configure(height=2, width=25)
        b3.configure(activebackground="#3777ac")
        b3.configure(highlightcolor="black")
        b2.configure(pady="5")
        b3.pack(anchor="s")

        #root.mainloop()

class valid():

    def __init__(self):
        try:
            global room
            roomno = int(room.get())
        except:
            messagebox.showinfo('Information','Invalid room no')

        r_list1 = [101,201,301,401]
        r_list2 = [102,202,302,402]
        r_list3 = [103,203,303,403]
        r_list4 = [104,204,304,404]

        if len(room.get()) > 3:
            messagebox.showinfo('Information','Invalid room no')
        elif len(room.get()) < 3:
            messagebox.showinfo('Information','Invalid room no')
        elif re.match('^[1-4]0[1-4]$',room.get()):

            cur.execute("select * from todo")
            rows = cur.fetchall()
            r = list()
            d = dict()

            for row in rows:
                r.append(row[0])
                d[row[0]] = row[4]

            #print(r)
            if roomno in r and d[roomno]=="in progress":
                    messagebox.showinfo('Information','Work in progress')
            else:
                global typee
                if roomno in r_list1:
                    typee = "Single"
                    #print(typee)
                elif roomno in r_list2:
                    typee = "Double"
                    #print(typee)
                elif roomno in r_list3:
                    typee = "Twin"
                    #print(typee)
                elif roomno in r_list4:
                    typee = "Suite"
                    #print(typee)

                m = menu()
        else:
            messagebox.showinfo('Information','Invalid room no')

class guest():

    def __init__(self):
        global room_no_win
        room_no_win = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        
        room_no_win.geometry("240x240+540+110")
        room_no_win.maxsize(240,240)
        room_no_win.minsize(240,240)
        room_no_win.title("ROOM NO")
        room_no_win.configure(background="#d9d9d9")
        room_no_win.configure(highlightbackground="#d9d9d9")
        room_no_win.configure(highlightcolor="black")



        self.Frame1 = Frame(room_no_win)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)


        self.Message6 = Label(self.Frame1,text="ENTER ROOM NO")
        self.Message6.pack(side=TOP,fill=X)
        

        global room
        room = StringVar()
        roomno = Entry(self.Frame1,text="",width=10,textvariable=room)
        roomno.pack(padx=20,pady=10)

        submit = Button(self.Frame1,text="Submit",command=valid)
        submit.place(relx=0.08, rely=0.27, relheight=0.15, relwidth=0.26)

        exitbtn = Button(self.Frame1,text="Exit",command=room_no_win.destroy)
        exitbtn.place(relx=0.66, rely=0.27, relheight=0.15, relwidth=0.26)

        room_no_win.mainloop()


if __name__ == '__main__':
    room=guest()