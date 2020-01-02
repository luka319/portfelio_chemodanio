import sqlite3

from pony.orm import *
db = Database()

class Person(db.Entity):
     name = Required(str)
     age = Required(int)

db.bind('sqlite', "./abc4.db", create_db=True)

db.generate_mapping(create_tables=True)

with db_session:
    p1 = Person(name='John', age=20)
    p1 = Person(name='John', age=20)
    p2 = Person(name='Mary', age=22)
    p3 = Person(name='Bob', age=30)


    select(p for p in Person).order_by(Person.name).show() 
    #spisok = select(p for p in Person).order_by(Person.name)

