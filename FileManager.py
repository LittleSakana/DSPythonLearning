# 文件读写

import os
def getCurrentPath():
    path = os.getcwd() # 获取绝对路径
    print(path)
    path1 = os.path.abspath(path) # 获取绝对路径
    print(path1)
    print(os.path.isabs(path)) # 路径是否是绝对路径
    print(os.path.split(path)) # 返回dirname和basename组成的元组
    print(os.path.getsize(path)) # 获取文件路径下文件的大小，单位字节
    print(os.listdir(path)) # 获取文件路径下所有文件的文件名数组

def getTotalSize():
    path = os.getcwd()
    totalSize = 0
    for fileName in os.listdir(path):
        tempsize = os.path.getsize(os.path.join(path,fileName))
        totalSize += tempsize
    print(totalSize)

def readAndWriteFile():
    path = os.getcwd()
    helloFile = open(os.path.join(path, 'hello'), 'r') # 得到文件对象，只读模式
    helloContent = helloFile.read() # 读取文件内容
    print(helloContent)
    helloContent1 = helloFile.readlines() # 按行读取文件内容，返回的是每一行组成的数组
    print(helloContent1)
    helloFile.close()

    writeFile = open(os.path.join(path, 'hello'), 'w') # 文件重写模式
    writeFile.write('\n Hello world!')
    writeFile.close()
    
    writeFile = open(os.path.join(path, 'hello'), 'a') # append 模式
    writeFile.write('\n Hello world!')
    writeFile.close()

    readFile = open(os.path.join(path, 'hello'), 'r')
    content = readFile.read()
    print(content)
    readFile.close()
    
#getCurrentPath()
#getTotalSize()
readAndWriteFile()
