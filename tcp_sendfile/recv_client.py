from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#端口重用

s.connect(('127.0.0.1',8888))



while True:
    data=input(">>")
    if data=='please send':
        s.send(data.encode())
        f=open('recv.jpg','wb')
        while True:
            img=s.recv(2049)
            if not img:
                break
            f.write(img)
        f.close()
    else:
        break


s.close()