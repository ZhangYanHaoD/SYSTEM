import os
import sys 
import subprocess
def restart():
    ret = subprocess.Popen(['python', os.path.abspath(__file__)])
    #说明:
    #当subprocess.Popen以列表作为参数时,列表内的每一个元素对应一个参数
    exit(0)

print("aaa!")
restart()
