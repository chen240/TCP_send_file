from socket import *

#创建套节字
s=socket(AF_INET,SOCK_DGRAM)

#
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

#固定接受端口
s.bind(('0.0.0.0',9999))

while True:
    try:
        msg,addr=s.recvfrom(1024)
        print("从{}获取信息:{}".\
            format(addr,msg.decode()))
    except (KeyboardInterrupt,SyntaxError):
        raise
    except Exception as e:
        print(e)
s.close()
