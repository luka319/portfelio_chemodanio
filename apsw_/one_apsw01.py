
import os, sys, time
import apsw

###
### Check we have the expected version of apsw and sqlite
###

print ("      Using APSW file",apsw.__file__              ) # from the extension module
print ("         APSW version",apsw.apswversion()         ) # from the extension module
print ("   SQLite lib version",apsw.sqlitelibversion()    ) # from the sqlite library code
print ("SQLite header version",apsw.SQLITE_VERSION_NUMBER ) # from the sqlite header file at compile time


###
### Opening/creating database
###

connection=apsw.Connection("dbfile.apsw_db")
cursor=connection.cursor()
###
### simple statement
###

cursor.execute("create table foo(x,y,z)")

###
### using different types
###

cursor.execute("insert into foo values(?,?,?)", (1, 1.1, None))  # integer, float/real, Null
cursor.execute("insert into foo(x) values(?)", ("abc", ))        # string (note trailing  comma to ensure tuple!)
                                                                

###
### multiple statements
###

cursor.execute("delete from foo; insert into foo values(1,2,3); \
   create table bar(a,b,c) ; insert into foo values(4, 'five', 6.0)")


for m,n,o in cursor.execute("select x,y,z from foo ; select a,b,c from bar"):
    print ( m,n,o)

print ("SQLite memory usage current %d max %d" % apsw.status(apsw.SQLITE_STATUS_MEMORY_USED))

# We can close connections manually (useful if you want to catch exceptions)
# but you don't have to
connection.close(True)  # force it since we want to exit


