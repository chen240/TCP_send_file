
from socket import *

s=socket()

#设置端口立即释放
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#获取套节字选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR,1))

#获取套节字地址族类型
print(s.family)

#获取套节字类型
print(s.type)

s.bind(('192.168.101.43',8888))
#获取绑定地址
print(s.getsockname())


#获取套节字文件描述符
print(s.fileno())

s.listen(5)
while True:
    c,addr=s.accept()
    print(c.getpeername())
    c.recv(1024)




