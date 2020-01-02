from sqlalchemy import create_engine
engine = create_engine('sqlite:///myfirst.db', echo=True, pool_recycle = 7200)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()

users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
     Column('fullname', String),
     Column('password', String)
     )

metadata.create_all(engine)



