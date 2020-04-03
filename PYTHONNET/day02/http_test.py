from socket import *

#创建tcp套节字
s=socket()

s.bind(('0.0.0.0',8000))
s.listen(5)

while True:
    c,addr=s.accept()
    print("Connect from",addr)

    data=c.recv(4096)
    print('**************************')
    print(data) #浏览器发来的http亲求
    print("**************************")

    #组织响应内容
    data='''HTTP/1.1 200 OK
    Content-Length: 705
    Content-Type: text/html

    <h1>welcom to tedu</h1>
    <p>这是一个测试你好</p>
    '''
    c.send(data.encode())
    c.close()
    
s.close()
