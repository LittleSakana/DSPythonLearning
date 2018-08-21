# 删除所有以.txt结尾的文件

import os

def deleteTextFiles():
    for fileName in os.listdir():
        if fileName.endswith('.txt'):
            os.unlink(fileName) # 删除文件

# 打印出所有的子文件夹、子文件
def printAllFiles():
    for folderName, subFolders, fileNames in os.walk(os.getcwd()):
        print('The current folder is ' + folderName)
        for subFolder in subFolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subFolder)
        for fileName in fileNames:
            print('FILE INSIDE ' + folderName + ': '+ fileName)

#deleteTextFiles()
printAllFiles()
