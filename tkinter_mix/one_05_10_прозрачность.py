# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

# класс главного окна
class main:

  count = 0

  def __init__(self, master):
    self.master = master
    self.master.title('parent')
    self.master.geometry('300x250+300+225')
    self.button = Button(self.master,
                         text = 'myButton',
                         command = self.open_child_win, font="Arial 20")
    self.button.pack(side = BOTTOM)


    # =============== class mixin ==============

    self.button2_transp = Button(self.master,
                         text = '<<< меньше прозрачность',
                         command = self.transparent_less, 
                         fg = 'red',
                         bg = 'yellow',
                         font="Arial 16")
    self.button2_transp.pack(side = TOP)


    self.button3_transp = Button(self.master,
                         text = 'больше прозрачность >>>',
                         command = self.transparent_more, 
                         fg = 'red',
                         bg = 'yellow',
                         font="Arial 16")
    self.button3_transp.pack(side = TOP)


    #root.wm_attributes('-alpha',0,3)
    self.master.mainloop()

  # =============== class mixin ==============
  d = 1.0
  def transparent_less(self):

    #root.wm_attributes('-alpha',0,3)
    if self.d <= 0.5:
       self.button2_transp.configure(text = '<<< дальше некуда!!!')

    else:
       if self.d > 0.6:
          self.button2_transp.configure(text = '<<< меньше призрачности')
       #self.button3_transp.configure(text = 'больше призрачности >>>')
       self.d = self.d - 0.1

    self.master.wm_attributes('-alpha',self.d)
    #w.attributes('-alpha', 0.1)
    print('self.d = ', self.d)

  def transparent_more(self):

    # self.button3_transp.configure(text = 'больше призрачности >>>')

    if self.d >= 1.0:
       self.button3_transp.configure(text = 'дальше некуда!!! >>>')

    else:
       if self.d < 0.8:
          self.button3_transp.configure(text = 'больше призрачности >>>')
       self.d = self.d + 0.1

    self.master.wm_attributes('-alpha',self.d)
    #w.attributes('-alpha', 0.1)
    print('self.d = ', self.d)




  def open_child_win(self):
    #self.count += self.count + 1
    self.count += 1
    child.counter = self.count
    ##print("child.counter = ", child.counter)
    child(self.master)

# класс дочерних окон

class child:


  def __init__(self, master):

    self.slave = Toplevel(master)
    self.slave.title('child')


    #self.counter += self.counter + 1

    self.label = Label(self.slave, text = ('Окно N '+str(self.counter)), font="Arial 18")
    #self.label = Label(self.slave, text = 'Привет, мир')
    #self.label.pack(padx = 0, pady = 0)
    self.label.pack(side = TOP)

    geometry1 = str(random.randrange(0,100))
    geometry2 = str(random.randrange(400,700))
    geometry11 = str(random.randrange(0,100))
    geometry22 = str(random.randrange(400,700))

    g1 = random.choice([geometry1,geometry2])
    g2 = random.choice([geometry11,geometry22])

    # geometry0 = '+'+geometry1+'+'+geometry2
    geometry0 = '+'+g1+'+'+g2
    geo = '200x150'+geometry0

    #self.slave.geometry('200x150+500+375')
    self.slave.geometry(geo)

    bgcolor = random.choice(colors)
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

# bgcolor = random.choice(colors)


# создание окна
root = Tk()

# запуск окна
main(root)

