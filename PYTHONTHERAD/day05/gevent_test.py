import gevent
from time import sleep

def foo(a,b):
    print("a=%d,b=%d"%(a,b))
    gevent.sleep(2)
    print("Runing foo again")

def bar():
    print("Running int bar")
    gevent.sleep(3)
    print("Running bar agin")

#生成协程
f=gevent.spawn(foo,1,2)
g=gevent.spawn(bar)
sleep(3)
print("===============")
gevent.joinall([f,g])
print("%%%%%%%%%%%%%%")