# ZIP Action

import zipfile

def compressFiles():
    newZip = zipfile.ZipFile('new.zip', 'w');
    newZip.write('1.txt', compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

def readZipFiles():
    testZip = zipfile.ZipFile('new.zip')
    print(testZip.namelist()) # 打印压缩文件内容
    textFile = testZip.getinfo('1.txt') # 获取文件信息
    print('压缩前大小：' + str(textFile.file_size))
    print('压缩后大小：'+ str(textFile.compress_size))
    testZip.close()

def extractZipFiles():
    testZip = zipfile.ZipFile('new.zip')
    testZip.extractall()
    testZip.close()
    
#compressFiles()
#readZipFiles()
extractZipFiles()
