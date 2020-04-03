import os
import signal

#向5557发送信号
os.kill(5557,signal.SIGKILL)