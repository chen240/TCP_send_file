from multiprocessing import Queue
from time import sleep

#创建队列
q=Queue(3)

q.put(1)

sleep(0.5)
print(q.empty())

q.put(2)
print(q.full())
# print(q.qsize())
q.put(3)
print(q.qsize())
# q.put(4,False)
print(q.get())
q.close() #关闭队列