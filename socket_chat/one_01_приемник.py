
import socket
from tkinter import *

tk = Tk()

"""
import imp
imp.reload(sys)
sys.setdefaultencoding("utf-8")
"""
#====================================

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind( ( '0.0.0.0', 8001 ) )

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

text01 = StringVar()
name01 = StringVar()

name01.set("Main Acad User")
text01.set("")

tk.title("Our Chat")

tk.geometry('400x300')

log = Text(tk, font="Arial 20")
nick = Entry(tk, textvariable = name01)
# msg = Entry(tk, textvariable=text01, bg='lightgreen', font="Arial 20")
msg = Entry(tk, textvariable=text01, bg='white', font="Arial 20")

msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both', expand='true')

def loopproc():
    log.see(END)
    s.setblocking(False)
    try:
        message = s.recv(128)
        message = message.decode('utf-8')
        print('message = ',message)
        log.insert(END, message+'\n')
        # log.insert(1.0, message+'\n')
    except:
        tk.after(1,loopproc)
        return
    tk.after(1, loopproc)
    return

#text02 = bytes(text01.get(), encoding="cp1251")
def sendproc(event):
    sock.sendto( bytes(name01.get().encode('utf-8'))+
         bytes(':'.encode('utf-8'))+bytes(text01.get().encode('utf-8')), 
              ('255.255.255.255', 8001) )
              # ('127.0.0.1', 8001) )
    #sock.sendto( name01.get()+':'+text02, ('255.255.255.255', 8001) )
    text01.set('')

msg.bind('<Return>', sendproc)

msg.focus_set()

tk.after(1, loopproc)
tk.mainloop()


