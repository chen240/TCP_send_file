import os,sys
from time import sleep

#结束后不再执行后面的内容
# os._exit(0)

try:
    sys.exit("hello world")  #进程的退出信息
except SystemExit as e:
    print("退出:",e)

print("process exit")