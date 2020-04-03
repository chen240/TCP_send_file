from socket import *
from select import *

#注册ＩＯ事件
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建poll对象
p=epoll()

#fileno---/home/tarena/桌面/第二阶段/PYTHONNET/day02/tcp_client.py
fdmap={s.fileno():s}


#注册关注的ＩＯ
p.register(s,EPOLLIN | EPOLLERR)

while True:
    #进行ＩＯ监控
    events=p.poll()
    for fd,event in events:
        if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print("Connect from",addr)
            p.register(c,POLLIN | POLLHUP)
            fdmap[c.fileno()]=c
        elif event & EPOLLIN:
            data=fdmap[fd].recv(1024)
            if not data:
                #客户端退出，从关注事件移除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send(b'Receive')




