
from pony.orm import *

db = Database()

db.bind(provider='sqlite', filename='pony(4)sqlite.db', create_db=True)

class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')

class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Required(Person)

db.generate_mapping(create_tables=True)

# =================================
from tkinter import *
from tkinter import messagebox
 
 
def to_db():

    with db_session:
                                                                    
         p1 = Person(name=name.get(), age=surname.get())                           

         select(p for p in Person).order_by(Person.name).show() 

 
root = Tk()
root.title("GUI на Python")
 
name = StringVar()
surname = StringVar()
 
name_label = Label(text="Введите имя:", font="Arial 18")
surname_label = Label(text="Возраст?:", font="Arial 18")
 
name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
 
name_entry = Entry(textvariable=name, font="Arial 18")
surname_entry = Entry(textvariable=surname, font="Arial 18")
 
name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)
 
 
message_button = Button(text="Click Me", command=to_db, font="Arial 18")
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()

# =================================
