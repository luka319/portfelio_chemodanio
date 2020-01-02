import datetime
import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'new_database',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)


# cnx = mysql.connector.connect(user='root', database='new_database')
cursor = cnx.cursor()

query = ("SELECT id, name FROM citys")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query)

for ( id_, name) in cursor:
  print("{}, {} kkk".format(
    id_, name))

cursor.close()
cnx.close()


#==========

