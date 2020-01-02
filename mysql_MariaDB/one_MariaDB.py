import mysql.connector as mariadb 
mariadb_connection = mariadb.connect(
        user='python_user', 
        password='some_pass', 
        database='employees') 

cursor = mariadb_connection.cursor() 

# - See more at: https://mariadb.com/resources/blog/how-connect-python-programs-mariadb#sthash.bItxCqjX.dpuf


