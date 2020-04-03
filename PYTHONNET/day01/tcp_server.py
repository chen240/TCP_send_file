#tcp_server.py
from socket import *

#创建套接字
sockfd=socket(AF_INET,SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',8888))

#设置监听
sockfd.listen(5)

#等待接受连接
print("Waiting for connect...")
connfd,addr=sockfd.accept()
print("Connect from",addr)

while True:
    #收发消息
    data=connfd.recv(1024)
    if data=="##":
        break
    print(data.decode())
    n=connfd.send(b'Receive your message')
    print("发送了%d字节" % n)


#关闭套节字
connfd.close()
sockfd.close()