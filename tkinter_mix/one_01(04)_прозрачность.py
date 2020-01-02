# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

#создание окна
root = Tk()
root.title('мое окно - myWindow')
#root.geometry('200x150+300+225')

root.geometry('250x350+250+225')

transparent = 1.0

def bubu():
    print('====== нажал кнопку =======')
    global transparent
    transparent -= 0.1
    root.wm_attributes('-alpha', transparent)
    print('trasparent = ', transparent)

button = Button(root,  
                text = 'уменьшить прозрачность', 
                command=bubu,  
                bg='yellow',
                fg='red',
                font= "Arial 18")
#button.pack(side = BOTTOM)
#button.pack(side = TOP)
button.pack(side = LEFT)
# вывод окна на экран
root.mainloop()


