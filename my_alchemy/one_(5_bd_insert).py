# from sqlalchemy import insert
from sqlalchemy import create_engine

engine = create_engine('sqlite:///myfirst2.db', echo=True, pool_recycle = 7200)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()

users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('fullname', String),
     Column('password', String)
     )

metadata.create_all(engine)

from sqlalchemy import insert

# insert into users (name, fullname) values ('Ivan', 'Poddubny');
abc1 = users_table.insert().values( 
         name = 'Ivan234',
         fullname = 'Poddybny567'
         )


abc2 = users_table.insert().values( 
         name = 'Ivan987',
         fullname = 'Vazov789'
         )

result1 = engine.execute(abc1)
result2 = engine.execute(abc2)


# Engine.execute() or Engine.connect()


'''
from sqlalchemy.sql import select
s = select([cookies])
rp = connection.execute(s)
results = rp.fetchall()
'''
