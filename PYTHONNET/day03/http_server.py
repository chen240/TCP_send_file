from socket import *


def handleClient(connfd):
    request=connfd.recv(4096)
    # print(request)
    #将request请求按照行分割
    request_lines=request.splitlines()
    for lines in request_lines:
        print(lines.decode())
    try:
        f=open("index.html")
    except IOError:
        response="HTTP/1.1 404 not found\r\n"
        response+="\r\n" #空行
        response+="===Sorry not found===="
    else:
        response="HTTP/1.1 200   OK\r\n"
        response+="\r\n" #空行
        response+=f.read()
    finally:
        #发送给浏览器
        connfd.send(response.encode())


#用来创建套节字
def main():
    sockfd=socket()
    sockfd.setsockopt\
    (SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8888))
    sockfd.listen(3)
    print("Listen to the port 8888")
    while True:
        connfd,addr=sockfd.accept()
        #处理请求
        handleClient(connfd)
        connfd.close()

if __name__ == "__main__":
    main()



