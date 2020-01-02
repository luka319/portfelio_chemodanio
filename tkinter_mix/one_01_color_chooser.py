# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

#создание окна
root = Tk()
root.title('мое окно - myWindow')
#root.geometry('200x150+300+225')

root.geometry('250x350+250+225')
#======================================
from tkinter import colorchooser

def my_color():

    color_my = colorchooser.askcolor()
    print(color_my)
    root.configure(bg=color_my[1])

#================
button_01 = Button(root,
                   text = 'нажми же меня',
                   command = my_color, 
                   font="Arial 24")

button_01.pack(side = BOTTOM)

# вывод окна на экран
root.mainloop()


