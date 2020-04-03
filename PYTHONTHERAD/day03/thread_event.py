import threading
from time import sleep

s=None
e=threading.Event()


def bar():
    print("bar半山头")
    global s
    s="天王该地胡"

def foo():
    print("说出口令就是自己人")
    sleep(2)
    if s=="天王盖地虎":
        print("我是座山掉，自己人")
    else:
        print("打死它")
    e.set()  #等foo验证完毕其他的再执行    

def fun():
    print("hehe...")
    sleep(1)
    global s
    s="小鸡吨蘑菇"


b=threading.Thread(target=bar)
f=threading.Thread(target=foo)
b.start()
f.start()
e.wait() #运行b f 之后其他内容不许执行


fun()
b.join()
f.join()