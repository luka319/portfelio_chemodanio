# coding:utf-8

import sys
ver=sys.version

if "2." in ver:
    from Tkinter import *
    print("tk = ", ver)
    import tkFileDialog as filedialog

elif "3." in ver:
    from tkinter import *
    print("tk = ", ver)
    from tkinter import filedialog


root=Tk("Text Editor")

text01=Text(root,
            font="Arial 18", 
            bg='lightgray', 
            fg='green')
text01.grid()
#======================

def save_as():
    global text01
    text = text01.get("1.0", "end-1c")

    save_file=filedialog.asksaveasfilename()

    #f01=open(savelocation, "w+")
    with open(save_file, "w+") as f01:

        f01.write(text)
        #f01.close()

button=Button(root, text="Save", 
                command=save_as, 
                font="Arial 18", 
                bg='yellow', 
                fg='red')

button.grid() 
#======================================================

def FontHelvetica():

    global text01
    text01.config(font="Helvetica")

def FontCourier():
    global text01
    text01.config(font="Courier")

#------------------------
font=Menubutton(root, text="Font",
                font="Arial 18", 
                # bg='yellow', 
                fg='blue')

font.grid() 
#------------------------

font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu

Helvetica=IntVar() 
arial=IntVar() 
times=IntVar() 
Courier=IntVar()

font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
command=FontHelvetica) 


root.mainloop()
