import requests, bs4
import sqlite3
import re
import time
connection = sqlite3.connect('ithappens.db')
cursor = connection.cursor()
cursor.executescript("""create table ithappy(
        id int auto_increment primary key, it_text longtext
    );""")
z=0
for kk in range(10):
    z=z+1
    s=requests.get('http://ithappens.me/random')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.text')  # <div class='text'>
    for x in p:        
        s=(x.getText().strip())
        # s=(x.getText())
        reg = re.compile('[^a-zA-Zа-яА-яЁё.,!]')
        s=reg.sub(' ', s)
        cursor.execute("INSERT INTO ithappy (it_text) VALUES ('"+s+"')")
        connection.commit()
    print(z)
connection.close()

