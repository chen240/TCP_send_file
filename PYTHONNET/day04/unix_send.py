from socket import *

#确保通行两端使用同一个套节字文件
sock_file="./sock_file"

#创建本地套节字
sockfd=socket(AF_UNIX,SOCK_STREAM)

#连接另一端
sockfd.connect(sock_file)

#收发消息
while True:
    msg=input(">>")
    if msg:
        sockfd.send(msg.encode())
        print(sockfd.recv(1024).decode())
    else:
        break

sockfd.close()







