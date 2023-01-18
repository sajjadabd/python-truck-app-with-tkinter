# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from tkinter.ttk import *

from tkinter import *

import threading

import sys

import operator

#import numpy as np





endThread = False
t = 'undefined'


def changeThreadToFalse() : 
    global endThread
    if endThread == False :
        endThread = True
    else :
        endThread = False


def set_interval(func, sec):
    global t
    if endThread == False :
        print('False')
    elif endThread == True :
        print('True')
        #t.cancel()
        #quit()
        #window.destroy()
        #close()
        #os._exit(0)
        #sys.exit()
        #return

    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
    
    
def hideOrShowWindow() :
    global endThread 
    #print(window.wm_state())
    if endThread == True :
        window.deiconify()
    else :
        if window.wm_state() == 'withdrawn':  # <----
            window.deiconify()
        else :
            window.withdraw()
    


#set_interval(hideOrShowWindow , 2)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.floater = FloatingWindow(self)

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)

        self.label = tk.Label(self, text="Click on the grip to move")
        self.grip = tk.Label(self, bitmap="gray25")
        self.grip.pack(side="left", fill="y")
        self.label.pack(side="right", fill="both", expand=True)

        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(x + 'x' + y)
        
        
        
        
        




def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
    
    
    
    




def showMessage():
    messagebox.showinfo('Message title', 'Message content')

#messagebox.askquestion('Message title','Message content')
#messagebox.askyesno('Message title','Message content')
#messagebox.askyesnocancel('Message title','Message content')
#messagebox.askokcancel('Message title','Message content')
#messagebox.askretrycancel('Message title','Message content')



def on_closing():
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    if t != 'undefined' :
        t.cancel()
    #quit()
    #close()
    #os._exit(0)
    #sys.exit()
    window.destroy()
    


def close():
    if t != 'undefined' :
        t.cancel()
    window.destroy()

window = Tk()
window.title("محموله ورودی")



s = ttk.Style()
s.theme_use('classic')

#frame = ttk.Frame(window, padding=20)
#window.grid()
label_section = Label(window, text="محموله ی ورودی سکشن" , font=('Tahoma',12) , pady=10 )
label_section.configure(bg='#333', fg='white')
label_section.pack_propagate(0)
label_section.pack(fill="both", expand=1)


label_barmill = Label(window, text="محموله ی ورودی بارمیل" , font=('Tahoma',12) , pady=10)
label_barmill.configure(bg='#333', fg='white')
label_barmill.pack_propagate(0)
label_barmill.pack(fill="both", expand=1)


#ttk.Label(frame, text="Hello World!").grid(column=0, row=1)
button = Button(window, text="مرسی", command=close , font=('Tahoma',12))

button.configure(
bg='#333', 
fg='white' , 
activebackground ='#222' ,
activeforeground ='white'
)

button.pack_propagate(0)
button.pack(fill="both", expand=1)

#e1 = Entry(frame).grid(row=0, column=1)
#e2 = Entry(frame).grid(row=1, column=1)

"""
def move_window(event):
    deltax = event.x - window.winfo_x()
    deltay = event.y - window.winfo_y()
    print(f'+{event.x_root}+{event.y_root}')
    window.geometry(f'+{event.x_root}+{event.y_root}')
    #window.geometry(f'+{event.x}+{event.y}')
"""


        

window.geometry('400x140')
window.resizable(0 , 0)
#window.maxsize(350, 100)
#window.minsize(350, 100)
#Start the event loop.

window.lift()
window.attributes('-topmost',True)
#window.wm_attributes('-fullscreen','true')
window.overrideredirect(True)
#window.bind("<B1-Motion>", move_window )
center(window)

# Hide it with .withdraw
#root.withdraw()
# To reveal it again:
#root.deiconify()





window.protocol("WM_DELETE_WINDOW", on_closing)



mainloop()


#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/toplevel.html
#pip install ttkthemes