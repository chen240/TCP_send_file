import os
from time import sleep

pid=os.fork()

if pid<0:
    print("create process failed")
elif pid==0:
    sleep(3)
    print("Child process exit",os.getpid())
    os._exit(3)

else:
    pid,ststus=os.wait()
    print(pid,ststus)
    print(os.WEXITSTATUS(status)) #获取子进程退出状态
    while True:
        pass