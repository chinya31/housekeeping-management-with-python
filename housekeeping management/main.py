import os
from subprocess import call

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

'''space for calling other pages'''
def click_guest_login():
    call(["python", "guest.py"])

def click_maid_login():
    call(["python", "stafflogin.py"])
    
def click_admin_login():
    call(["python", "admin_login.py"])


class HOUSEKEEPING:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        

        root.geometry("963x749+540+110")
        root.maxsize(963,749)
        root.minsize(963,749)
        root.title("HOUSEKEEPING MANAGEMENT")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)


        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="#d9d9d9")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''WELCOME''')
        self.Message6.configure(width=791)



        self.admin_login = Button(self.Frame1)
        self.admin_login.place(relx=0.18, rely=0.17, height=103, width=566)
        self.admin_login.configure(activebackground="#d9d9d9")
        self.admin_login.configure(activeforeground="#000000")
        self.admin_login.configure(background="#d9d9d9")
        self.admin_login.configure(disabledforeground="#bfbfbf")
        self.admin_login.configure(font=font14)
        self.admin_login.configure(foreground="#000000")
        self.admin_login.configure(highlightbackground="#d9d9d9")
        self.admin_login.configure(highlightcolor="black")
        self.admin_login.configure(pady="0")
        self.admin_login.configure(text='''1.ADMIN LOGIN''')
        self.admin_login.configure(width=566)
        self.admin_login.configure(command=click_admin_login)


        self.guest_login = Button(self.Frame1)
        self.guest_login.place(relx=0.18, rely=0.33, height=93, width=566)
        self.guest_login.configure(activebackground="#d9d9d9")
        self.guest_login.configure(activeforeground="#000000")
        self.guest_login.configure(background="#d9d9d9")
        self.guest_login.configure(disabledforeground="#bfbfbf")
        self.guest_login.configure(font=font14)
        self.guest_login.configure(foreground="#000000")
        self.guest_login.configure(highlightbackground="#d9d9d9")
        self.guest_login.configure(highlightcolor="black")
        self.guest_login.configure(pady="0")
        self.guest_login.configure(text='''2.GUEST''')
        self.guest_login.configure(width=566)
        self.guest_login.configure(command=click_guest_login)


        self.maid_login = Button(self.Frame1)
        self.maid_login.place(relx=0.18, rely=0.47, height=93, width=566)
        self.maid_login.configure(activebackground="#d9d9d9")
        self.maid_login.configure(activeforeground="#000000")
        self.maid_login.configure(background="#d9d9d9")
        self.maid_login.configure(disabledforeground="#bfbfbf")
        self.maid_login.configure(font=font14)
        self.maid_login.configure(foreground="#000000")
        self.maid_login.configure(highlightbackground="#d9d9d9")
        self.maid_login.configure(highlightcolor="black")
        self.maid_login.configure(pady="0")
        self.maid_login.configure(text='''3.STAFF LOGIN''')
        self.maid_login.configure(width=566)
        self.maid_login.configure(command=click_maid_login)


        self.exit_btn = Button(self.Frame1)
        self.exit_btn.place(relx=0.18, rely=0.61, height=103, width=566)
        self.exit_btn.configure(activebackground="#d9d9d9")
        self.exit_btn.configure(activeforeground="#000000")
        self.exit_btn.configure(background="#d9d9d9")
        self.exit_btn.configure(disabledforeground="#bfbfbf")
        self.exit_btn.configure(font=font14)
        self.exit_btn.configure(foreground="#000000")
        self.exit_btn.configure(highlightbackground="#d9d9d9")
        self.exit_btn.configure(highlightcolor="black")
        self.exit_btn.configure(pady="0")
        self.exit_btn.configure(text='''4.EXIT''')
        self.exit_btn.configure(width=566)
        self.exit_btn.configure(command=quit)


        root.mainloop()



if __name__ == '__main__':
    GUEST=HOUSEKEEPING()