from socket import *

s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)#端口重用

s.bind(('127.0.0.1',8888))
s.listen(5)
while True:
    c,addr=s.accept()
    print("Connect from",addr)

    # f=open("send.jpg",'rb')

    while True:
        data=c.recv(1024).decode()
        if not data:
            break
        elif data=="please send":
            f=open('send.jpg','rb')
            while True:
                img=f.read(2049)
                if not img:
                    break
                c.send(img)
                
            f.close()

    c.close()
s.close()