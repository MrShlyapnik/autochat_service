from datetime import time

import psutil
import os
import time
import subprocess
# from cffi.setuptools_ext import execfile
print("Start")
pid = -1
celery_pid = -1
while True:
    count = 0
    celery = 0
    for proc in psutil.process_iter():
        name = proc.name()
        if proc.pid == pid:
            count = 1

    if count == 0:
        cmd = 'python3 main.py'
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True)
        p.wait()
        pid = p.pid
        print("Start.py")
    time.sleep(600)
