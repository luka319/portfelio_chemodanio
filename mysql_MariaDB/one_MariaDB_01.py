import mysql.connector as mariadb 

mariadb_connection = mariadb.connect(
        user='root', 
        password='', 
        database='new_database') 

cursor2 = mariadb_connection.cursor() 

# - See more at: https://mariadb.com/resources/blog/how-connect-python-programs-mariadb#sthash.bItxCqjX.dpuf

cursor2.execute("select * from citys;")
cursor2.execute("show tables;")

for id, name in cursor2: 
     print("id: {}, name: {}").format(id,name) 








