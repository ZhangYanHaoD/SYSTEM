import win32api
import sys
DAEMON_PATH="D:\\vscode\\SYSTEM\\daemon.py"
win32api.ShellExecute(None,"runas", sys.executable, "sc create serviceName binPath="+DAEMON_PATH+" start= auto", None, 1)
