# -*- coding: utf-8 -*-
# импортирование модулей python
from tkinter import *

# класс главного окна
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('parent')
    self.master.geometry('200x150+300+225')
    self.button = Button(self.master,
                         text = 'myButton',
                         command = self.openDialog,
                         font = "Verdana 18")
    self.button.pack(side = BOTTOM)
    self.master.mainloop()

  def openDialog(self):
    child(self.master)

import random

# класс дочерних окон

counter = 0

class child:
  def __init__(self, master):
    self.slave = Toplevel(master)
    self.slave.title('child')

    global counter
    #counter = counter + 1
    counter += 1

    self.label = Label(self.slave,
                       text = 'окно N '+str(counter),
                       font = "Verdana 18")
    self.label.pack(side = TOP)

    a1 = random.randint(1, 250)
    a11 = random.randint(450, 600)

    b2 = random.randint(1, 250)
    b22 = random.randint(450, 600)

    a = random.choice([a1,a11])
    b = random.choice([b2,b22])

    #kkk = '500+375'
    kkk = str(a)+'+'+str(b)
    self.slave.geometry('200x150+' + kkk)
    # self.slave.geometry('200x150+500+375')

    #self.slave.configure(bg="#afd490")
    #self.slave.configure(bg="red")
#========================================
    bgcolor = random.choice(colors) 
    print("bgcolor = ", bgcolor)    

    self.slave.configure(bg=bgcolor)
    #self.slave.configure(bg='green')
    #root.configure(bg='green')


import random
colors = ['red','yellow', 'green', 'orange', 
          'aqua', 'blue', 'fuchsia', 'maroon', 
          'pink', 'purple', 'lime',
          'violet', 'cyan', 'cornflowerblue',
          'indigo', 'chartreuse'
         ]


# создание окна
root = Tk()

# запуск окна
main(root)
