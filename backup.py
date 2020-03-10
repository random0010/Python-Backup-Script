import configparser
import shutil
import errno
import os
import ctypes
from datetime import datetime


def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Error: %s' % e)


config = configparser.ConfigParser()
config.read("./config.ini")

print("Backup is starting")

now = datetime.now()
backupDir = config.items('DEST')[0][1] + "\\backup_" + now.strftime("%d-%m-%Y_%Hh%Mm%Ss")
print(config.items('DEST')[0][1])

if not os.path.exists(backupDir):
    os.makedirs(backupDir)

for i in range(0, len(config.items('PATH'))):
    folder = config.items('PATH')[i][1]
    folderName = config.items('PATH')[i][1].split('\\')[len(config.items('PATH')[i][1].split('\\')) - 1]

    destination = backupDir + "\\" + folderName
    print("Backup in progress : " + folder)

    copy(folder, destination)


ctypes.windll.user32.MessageBoxW(0, "Backup is finish", "Success !", 64)