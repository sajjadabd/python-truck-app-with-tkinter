# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import threading
import sys
import operator
import json
from datetime import date
import jdatetime

#today = date.today()
today = jdatetime.date.today()


today = today.strftime("%Y/%m/%d")

#print(today)

#import urllib.request as fetch
#text = fetch.urlopen("http://172.16.32.4:81/api/BilletInput/GetBilletInputs/?username=6272&password=sj6272&startDate=1401/08/17&endDate=1401/08/17").read()
#print(text)






#from tkextrafont import Font

#import numpy as np


#myFont = 'Shabnam.ttf'
#font = Font(file="./Shabnam.ttf", family="Shabnam")

myFont = 'Shabnam'
fontSize = 14

endThread = False
t = 'undefined'


sectionMillCounterAll = 0
barMillCounterAll = 0


sectionMillCounter = 0
barMillCounter = 0

sectionMillMessage = ''
barMillMessage = ''


trucks = []
result = []

import urllib3
http = urllib3.PoolManager()
import requests

url = "http://172.16.32.4:81/api/BilletInput/GetBilletInputs/?username=6272&password=sj6272&startDate="+ today + "&endDate=" + today 
#print(url)


#print(result)





        



"""
print("----------------------------")
"""


    
def updateCounters() :

    global sectionMillCounter
    global sectionMillCounterAll
    
    global barMillCounter
    global barMillCounterAll
    
    global result
    global trucks
    
    sectionMillCounterAll = 0
    barMillCounterAll = 0
    
    
    

    for eachNewTruck in result :
        if eachNewTruck["BilletType"].lower() == "3sp" :
            sectionMillCounterAll+=1
        else :
            barMillCounterAll+=1
        

    counter = 0
    while counter < len(result) :
        #print(counter)
        if counter < len(trucks) :
            pass 
        else :
            if result[counter]["BilletType"].lower() == "3sp" :
                sectionMillCounter+=1 
            else :
                barMillCounter+=1
        counter += 1
        



def changeThreadToFalse() : 
    global endThread
    if endThread == False :
        endThread = True
    else :
        endThread = False


def set_interval(func, sec):
    global t

    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
    
    
def hideOrShowWindow() :
    #print(window.wm_state())
    global result
    global trucks
    #print(len(result) , len(trucks))
    if len(result) > len(trucks) :
        window.deiconify()
    else :
        pass
        #if window.wm_state() == 'withdrawn':  # <----
        #    window.deiconify()
        #else :
        #    window.withdraw()





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




window = Tk()
window.title("???????????? ??????????")





def close():
    #if t != 'undefined' :
    #    t.cancel()
    #window.destroy()
    sectionMillCounter = 0
    barMillCounter = 0
    window.withdraw()
    
    

def on_closing():
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #if t != 'undefined' :
    #    t.cancel()
    #quit()
    #close()
    #os._exit(0)
    #sys.exit()
    #window.destroy()
    close()




    


s = ttk.Style()
s.theme_use('alt')
s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Shabnam', 8)) # Modify the font of the body
s.configure("mystyle.Treeview.Heading", font=('Shabnam', 8)) # Modify the font of the headings
s.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


#frame = ttk.Frame(window, padding=20)
#window.grid()


label_section = Label()
treeSection = ttk.Treeview()
label_barmill = Label()
treeBarmill = ttk.Treeview()
button = Button()

sectionMillMessage = ''
barMillMessage = ''

def designWindow() :
    global label_section
    global label_barmill
    global treeSection
    global treeBarmill
    global button
    
    global sectionMillMessage
    global barMillMessage
    
    global myFont 
    global fontSize
    
    global trucks
    global result 
    
    global sectionMillCounter
    global barMillCounter
    
    
    
    diff = len(result) - len(trucks)
    
    defaultHeightForSectionTable = 3
    defaultHeightForBarMillTable = 3
    
    if diff >= 5 : 
        diff = 5
    
    
    if sectionMillCounter >= 5 : 
        defaultHeightForSectionTable = 5
    else :
        defaultHeightForSectionTable = sectionMillCounter
        
    if barMillCounter >= 5 : 
        defaultHeightForBarMillTable = 5
    else :
        defaultHeightForBarMillTable = barMillCounter

    
    windowWidth = fontSize * (60)
    windowHeight = fontSize * (25+diff)
    
    label_section = Label(window, text=sectionMillMessage , font=(myFont,fontSize) , pady=fontSize )
    label_section.configure(bg='#333', fg='white')
    label_section.pack_propagate(0)
    label_section.pack(fill="both", expand=1)





    treeSection = ttk.Treeview(
        window , 
        style="mystyle.Treeview" , 
        column=("truckCode","FName", "LName", "Roll No" , "Description"  , "Counter" ),
        show='headings' , 
        height=defaultHeightForSectionTable  
    )


    treeSection.column("# 1", anchor=CENTER , width = 50  )
    treeSection.heading("# 1", text="?????????? ????????" )
    treeSection.column("# 2", anchor=CENTER , width = 2)
    treeSection.heading("# 2", text="?????????? ????????")
    treeSection.column("# 3", anchor=CENTER , width = 30)
    treeSection.heading("# 3", text="??????????????" )
    treeSection.column("# 4", anchor=CENTER )
    treeSection.heading("# 4", text="?????????? ??????????")
    treeSection.column("# 5", anchor=CENTER , width = 20)
    treeSection.heading("# 5", text="?????? ????????")
    treeSection.column("# 6", anchor=CENTER , width = 2)
    treeSection.heading("# 6", text="??????????")

    # Insert the data in Treeview widget
    
    counter = 0
    insideCounter = 1
    while counter < len(result) :
        #print(counter)
        if counter < len(trucks) :
            pass 
        else :
            if result[counter]["BilletType"].lower() == "3sp" :
                #print (result[counter])
                treeSection.insert('', 'end', text="1", values=(
                        result[counter]["Number"],
                        result[counter]["BilletInputCount"], 
                        result[counter]["Employer"] , 
                        result[counter]["BilletDescription"] ,                       
                        result[counter]["BilletType"] , 
                        str(insideCounter) 
                    ) 
                )
                insideCounter+=1
            else :
                pass
        counter += 1
        
    


    treeSection.pack_propagate(0)
    treeSection.pack(fill=BOTH, expand=1)




    label_barmill = Label(window , text=barMillMessage , font=(myFont,fontSize) , pady=fontSize)
    label_barmill.configure(bg='#333', fg='white')
    label_barmill.pack_propagate(0)
    label_barmill.pack(fill="both", expand=1)



    treeBarmill = ttk.Treeview(
        window , 
        style="mystyle.Treeview" , 
        column=("truckCode","FName", "LName", "Roll No" , "Description"  , "Counter" ),
        show='headings' , 
        height=defaultHeightForBarMillTable
    )


    treeBarmill.column("# 1", anchor=CENTER , width = 50  )
    treeBarmill.heading("# 1", text="?????????? ????????" )
    treeBarmill.column("# 2", anchor=CENTER , width = 2)
    treeBarmill.heading("# 2", text="?????????? ????????")
    treeBarmill.column("# 3", anchor=CENTER , width = 30)
    treeBarmill.heading("# 3", text="??????????????" )
    treeBarmill.column("# 4", anchor=CENTER )
    treeBarmill.heading("# 4", text="?????????? ??????????")
    treeBarmill.column("# 5", anchor=CENTER , width = 20)
    treeBarmill.heading("# 5", text="?????? ????????")
    treeBarmill.column("# 6", anchor=CENTER , width = 2)
    treeBarmill.heading("# 6", text="??????????")

    # Insert the data in Treeview widget
    counter = 0
    insideCounter = 1
    while counter < len(result) :
        #print(counter)
        #print(result[counter]["BilletType"].lower())
        if counter < len(trucks) :
            pass 
        else :
            if result[counter]["BilletType"].lower() == "3sp" :
                pass
            else :
                #print(result[counter])
                treeBarmill.insert('', 'end', text="1", values=(
                        result[counter]["Number"],
                        result[counter]["BilletInputCount"], 
                        result[counter]["Employer"] , 
                        result[counter]["BilletDescription"] ,  
                        result[counter]["BilletType"] , 
                        str(insideCounter) 
                    ) 
                )
                insideCounter+=1
        counter += 1


    treeBarmill.pack_propagate(0)
    treeBarmill.pack(fill=BOTH, expand=1)





    #ttk.Label(frame, text="Hello World!").grid(column=0, row=1)
    button = Button(window, text="??? ???????? ???", command=close , font=(myFont,fontSize) , cursor='hand2')

    button.configure(
        bg='#333', 
        fg='white' , 
        activebackground ='#222' ,
        activeforeground ='white'
    )

    button.pack_propagate(0)
    button.pack(fill="both", expand=1)
    
    
    label_section.bind("<B1-Motion>", move_window )
    label_section.bind("<ButtonRelease-1>" , release_window)
    label_section.bind("<Button-1>", start_drag)
    
    
    
    
    
    window.geometry(str(windowWidth) + 'x' + str(windowHeight))
    # end of design window 



#e1 = Entry(frame).grid(row=0, column=1)
#e2 = Entry(frame).grid(row=1, column=1)

startDragX = 'undefined'
startDragY = 'undefined'



def move_window(event):
    #print(event.x , event.y)
    #print(event.x_root , event.y_root)
    #print(window.winfo_x() , window.winfo_y())
    deltax = event.x_root - event.x # - window.winfo_x()
    deltay = event.y_root - event.y # - window.winfo_y()
    #print(window.winfo_x() , event.x_root ,  event.x , deltax )
    #print(type(window.winfo_x()) , type(event.x) , type(deltax))
    finalX = int(event.x_root) - int(deltax) #+ int(deltax)
    finalY = int(event.y_root) + int(deltay) # + int(deltay)
    #print(f'+{event.x_root}+{event.y_root}')
    #print(event.y_root + (startDragY))
    window.geometry(f'+{event.x_root - startDragX}+{event.y_root - startDragY - 5}')
    #window.geometry(f'+{event.x}+{event.y}')


def release_window(event) :
    center(window)
    
def start_drag(event) :
    global startDragX
    global startDragY
    startDragX = event.x 
    startDragY = event.y


windowWidth = fontSize * 60
windowHeight = fontSize * 25

window.geometry(str(windowWidth) + 'x' + str(windowHeight))
window.resizable(0 , 0)
#window.maxsize(350, 100)
#window.minsize(350, 100)
#Start the event loop.

window.lift()
window.attributes('-topmost',True)
#window.wm_attributes('-fullscreen','true')
window.overrideredirect(True)





#https://www.plus2net.com/python/tkinter-events.php
""" Event Binding
<Button-1>	Mouse Left button click
<Button-2>	Mouse center button click
<Button-3>	Mouse Right button click
<B1-Motion>	Mouse Left button Press and move
<ButtonRelease-1>	Mouse Left button release, ButtonRelease-2 for Middle and 3 for right button.
<Double-Button-1>	Left Mouse key is double clicked.
<Enter>	Mouse Entry over a widget
<Leave>	Mouse Leave a widget
<MouseWheel>	Mouse Wheel Up or Down rotation
"""



center(window)

# Hide it with .withdraw
#root.withdraw()
# To reveal it again:
#root.deiconify()

window.protocol("WM_DELETE_WINDOW", on_closing)









    
    



#print(len(result))









def hideWindow() :
    window.withdraw() 
    
    
def showWindow() :
    window.deiconify() 
    



def updateProgramLabelsAndShowWindow() :
    global sectionMillCounter
    global sectionMillCounterAll
    
    global barMillCounter
    global barMillCounterAll
    
    global label_section
    global label_barmill
    
    global sectionMillMessage
    global barMillMessage

    if sectionMillCounterAll == 0 :
        sectionMillMessage = '?????? ?????????? ???? ?????? ????????' + '.....' + ' ?????????? ?????????? : ' + str(sectionMillCounterAll)  ;
    else :
        sectionMillMessage = '?????????? ' +	str(sectionMillCounter) + ' ?????? ?????????? ' + '???? ?????? ???????? ' + '???????? ???? ' + '.....' + ' ?????????? ?????????? : ' + str(sectionMillCounterAll)   ;
    
    
    
    if barMillCounterAll == 0 :
        barMillMessage = '?????? ?????????? ???? ?????? ????????????' + '.....' + ' ?????????? ?????????? : ' + str(barMillCounterAll)  ;
    else :
        barMillMessage = "?????????? " +	str(barMillCounter) + " ?????? ?????????? " + "???? ?????? ???????????? " +"???????? ???? " + '.....' + ' ?????????? ?????????? : ' + str(barMillCounterAll)  ;
        
    #print('sectionMillCounterAll ' , sectionMillCounterAll)    
    #print('barMillCounterAll ' , barMillCounterAll)
    

    label_section.config(text=sectionMillMessage)
    label_barmill.config(text=barMillMessage)
    


def clearWindow() :
    global label_section
    global label_barmill
    global treeSection
    global treeBarmill
    global button
    
    label_section.pack_forget()
    label_barmill.pack_forget()
    treeSection.pack_forget()
    treeBarmill.pack_forget()
    button.pack_forget()
    




def checkForTruckUpdates() :
    global result
    global trucks
    r = requests.get(url)
    data = json.loads(r.text)
    result = data["Result"]
    #print(result)
    if len(result) > len(trucks) :
        updateCounters()
        updateProgramLabelsAndShowWindow()
        clearWindow()
        designWindow()
        hideOrShowWindow()
        trucks = result
    else : 
        pass


set_interval(checkForTruckUpdates , 10)
    
    
hideWindow()


mainloop()


#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/toplevel.html
#pip install ttkthemes