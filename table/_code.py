import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import threading



t = 'undefined' # for threading

myFont = 'Shabnam'
fontSize = 14

def set_interval(func, sec):
    global t
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
    
    
def hideOrShowWindow() :
    print(window.wm_state())
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
        self.geometry(f"+{x}+{y}")
        
        
        
        
        




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

def close():
    if t != 'undefined' :
        t.cancel()
    window.destroy()


# take the data
lst = [(1,'آرش','تهران',19),
	(2,'کاوه','ساری',18),
	(3,'فریدون','یزد',20),
	(4,'سهراب','تبریز',21),
	(5,'زال','سنندج',21)]
    
    
window = Tk()
window.title("محموله ورودی")


#style = ttk.Style()
#style.theme_use('clam')

s = ttk.Style()
s.theme_use('clam')
#style.theme_use('clam')
#style.theme_use('alt')
#style.theme_use('classic')
#style.theme_use('vista')
#style.theme_use('xpnative')
#style.theme_use('winnative')

#frame = ttk.Frame(window, padding=20)
#window.grid()
#.pack(fill=BOTH,side=TOP, expand=YES)
window.configure(bg='#333')
#window.grid()
label_section = Label(window, text="محموله ی ورودی سکشن" , font=(myFont,fontSize) , pady=10 )
label_section.configure(bg='#333', fg='white')
#label_section.grid(row = 0 , column = 0 , columnspan=4)
label_section.pack_propagate(0)
label_section.pack(fill="both", expand=1)





treeSection = ttk.Treeview(window, column=("truckCode","FName", "LName", "Roll No"),
show='headings' , height=4 )


treeSection.column("# 1", anchor=CENTER , width = 50)
treeSection.heading("# 1", text="شماره پلاک")
treeSection.column("# 2", anchor=CENTER , width = 20)
treeSection.heading("# 2", text="تعداد بیلت")
treeSection.column("# 3", anchor=CENTER)
treeSection.heading("# 3", text="فرستنده")
treeSection.column("# 4", anchor=CENTER , width = 20)
treeSection.heading("# 4", text="نوع بیلت")

# Insert the data in Treeview widget
treeSection.insert('', 'end', text="1", values=('111','Amit', 'Kumar', '17701'))
treeSection.insert('', 'end', text="2", values=('111','Ankush', 'Mathur', '17702'))
treeSection.insert('', 'end', text="3", values=('111','Manisha', 'Joshi', '17703'))
treeSection.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeSection.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeSection.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeSection.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeSection.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeSection.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))

treeSection.pack_propagate(0)
treeSection.pack(fill=BOTH, expand=1)








label_barmill = Label(window, text="محموله ی ورودی بارمیل" , font=(myFont,fontSize) , pady=10)
label_barmill.configure(bg='#333', fg='white')
#label_barmill.grid(row = 1 + len(lst) + 1 , column = 0 , columnspan=4)
label_barmill.pack_propagate(0)
label_barmill.pack(fill="both", expand=1)




treeBarmill = ttk.Treeview(window, column=("truckCode","FName", "LName", "Roll No"),
show='headings' , height=4 )


treeBarmill.column("# 1", anchor=CENTER , width = 50)
treeBarmill.heading("# 1", text="شماره پلاک")
treeBarmill.column("# 2", anchor=CENTER , width = 20)
treeBarmill.heading("# 2", text="تعداد بیلت")
treeBarmill.column("# 3", anchor=CENTER)
treeBarmill.heading("# 3", text="فرستنده")
treeBarmill.column("# 4", anchor=CENTER , width = 20)
treeBarmill.heading("# 4", text="نوع بیلت")

# Insert the data in Treeview widget
treeBarmill.insert('', 'end', text="1", values=('111','Amit', 'Kumar', '17701'))
treeBarmill.insert('', 'end', text="2", values=('111','Ankush', 'Mathur', '17702'))
treeBarmill.insert('', 'end', text="3", values=('111','Manisha', 'Joshi', '17703'))
treeBarmill.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeBarmill.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeBarmill.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeBarmill.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeBarmill.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))
treeBarmill.insert('', 'end', text="4", values=('111','Shivam', 'Mehrotra', '17704'))

treeBarmill.pack_propagate(0)
treeBarmill.pack(fill=BOTH, expand=1)





#ttk.Label(frame, text="Hello World!").grid(column=0, row=1)
button = Button(window, text="♥ مرسی ♥", 
command=close , font=(myFont,fontSize), cursor='hand2')

"""
hand2
hand1
X_cursor
arrow
based_arrow_down
based_arrow_up
boat
bogosity
bottom_left_corner
bottom_right_corner
bottom_side
bottom_tee
box_spiral
center_ptr
circle
clock
coffee_mug
cross
cross_reverse
crosshair
diamond_cross
dot
dotbox
double_arrow
draft_large
draft_small
draped_box
exchange
fleur
gobbler
gumby
hand1
hand2
heart
icon
iron_cross
left_ptr
left_side
left_tee
leftbutton
ll_angle
lr_angle
man
middlebutton
mouse
pencil
pirate
plus
question_arrow
right_ptr
right_side
right_tee
rightbutton
rtl_logo
sailboat
sb_down_arrow
sb_h_double_arrow
sb_left_arrow
sb_right_arrow
sb_up_arrow
sb_v_double_arrow
shuttle
sizing
spider
spraycan
star
target
tcross
top_left_arrow
top_left_corner
top_right_corner
top_side
top_tee
trek
ul_angle
umbrella
ur_angle
watch
xterm

"""


button.configure(
bg='#333', 
fg='white' , 
activebackground ='#222' ,
activeforeground ='white' ,
)

button.pack_propagate(0)
button.pack(fill="both", expand=1)

#e1 = Entry(frame).grid(row=0, column=1)
#e2 = Entry(frame).grid(row=1, column=1)

startDragX = ''
startDragY = ''


def drag_start(event) :
    global startDragX
    global startDragY
    startDragX = int(event.x)
    startDragY = int(event.y)


def move_window(event):
    deltax = event.x - window.winfo_x()
    deltay = event.y - window.winfo_y()
    #print(type(startDragX) , type(startDragY))
    #return
    finalX = event.x_root - startDragX 
    finalY = event.y_root - startDragY - 6 
    window.geometry(f'+{finalX}+{finalY}')
    #window.geometry(f'+{event.x}+{event.y}')


def drag_end(event) :
    center(window)
        
        
        
def mouse_enter_button(event) :
    button.configure(
        bg='#222', 
        fg='white' , 
        activebackground ='#111' ,
        activeforeground ='white' ,
    )



def mouse_leave_button(event) :
    button.configure(
        bg='#333', 
        fg='white' , 
        activebackground ='#111' ,
        activeforeground ='white' ,
    )



window.geometry('600x440')
#window.resizable(0 , 0)
#window.maxsize(350, 100)
#window.minsize(350, 100)
#Start the event loop.

window.lift()
window.attributes('-topmost',True)
#window.wm_attributes('-fullscreen','true')
window.overrideredirect(True)


label_section.bind("<B1-Motion>", move_window )
label_section.bind("<Button-1>", drag_start )
label_section.bind("<ButtonRelease-1>", drag_end )

#label_barmill.bind("<B1-Motion>", move_window )
#label_barmill.bind("<Button-1>", drag_start )
#label_barmill.bind("<ButtonRelease-1>", drag_end )

#button.bind("<Enter>" , mouse_enter_button)
#button.bind("<Leave>" , mouse_leave_button)

center(window)

# Hide it with .withdraw
#root.withdraw()
# To reveal it again:
#root.deiconify()


"""

root.withdraw()
print(root.wm_state())
if root.wm_state() == 'withdrawn':  # <----
    root.iconify()

"""


""" Event Handling
<Button-1> left mouse button
<Button-2> middle mouse button
<Button-3> right mouse button
<Button-4> scroll up with mouse
<Button-5> scroll down with mouse


<Double-Button-1> double click left
<Double-Button-2> double click middle 
<Double-Button-3> double click right

<Enter> The mouse pointer entered the widget. 

<Leave> The mouse pointer left the widget.

<Return> The user pressed the Enter key

<Key> The user pressed any key.

<Shift-Up> The user pressed the Up arrow, while holding the Shift key pressed


<B1-Motion> left click drag

<Motion> mouse cursor moves across the designated widget.

<Button-{num}> mouse {num} has been clicked.

<ButtonRelease-{num}> mouse {num} has been released.

<MouseWheel> mouse wheel is scrolled

<Escape>

<Right> right arrow

"""



tableFontSize = 10
backgroundColor = '#222'

"""
def createTable() :
    global backgroundColor
    for i in range(total_rows):
        #frame = ttk.Frame(window)
        for j in range(total_columns):
            if i%2 == 0 :
                backgroundColor = '#111'
            else : 
                backgroundColor = '#333'
            

            theRow = Label(window, width=10, bg=backgroundColor,
            fg='white',font=('Shabnam',tableFontSize,'bold'),
            justify='right',pady=3, cursor='pirate')
            theRow.grid(row=i+1, column=j)
            theRow.config(text= lst[i][j] )
        #frame.grid(row = i)
"""

        


# find total number of rows and
# columns in list

#total_rows = len(lst)
#total_columns = len(lst[0])



#table = createTable()



window.mainloop()


#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/toplevel.html
#pip install ttkthemes