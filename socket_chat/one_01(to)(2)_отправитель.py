import socket
import math
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

b = 0
c = 0

while True:
      # sock.sendto('broadcast', ('255.255.255.255', 8001) )

      zz = input("напиши что-нибудь _ ")
      #print(zz.format(a[bb], c))

      sock.sendto(bytes(zz.encode('utf-8')), ('127.0.0.1', 8001) )
      time.sleep(0.5)




