
from socket import *

#创建套节字
sockfd=socket(AF_INET,SOCK_STREAM)

#发起连接
server_addr=('127.0.0.1',8888)
sockfd.connect(server_addr)

while True:
    #消息发送接受
    data=input("发送>>")
    sockfd.send(data.encode())
    if data == '##':
        break
    data=sockfd.recv(1024)
    print("接收到:",data.decode())


#关闭套节字
sockfd.close()