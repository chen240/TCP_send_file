from socket import *

s=socket()
s.connect(('192.168.101.43',8888))

f=open('send.jpg','rb')

while True:
    data=f.read(1024)
    if not data:
        break
    s.send(data)
f.close()
s.close()







