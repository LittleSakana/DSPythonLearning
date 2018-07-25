# 字符串处理

def handleString():
   print('picnicItems'.center(20,'-')) # 输出以指定字符串为中心的长度为20的字符串
   print('*'.ljust(15, '-') + 'Hello'.rjust(5))
   print('Hello'.ljust(15) + '*'.rjust(5))
   print('   \n\tHello'.strip())
   print('   \n\tHello'.lstrip()) # 去除左边的空格、换行、制表符
   print('   \n\tHello'.rstrip()) # 去除右边的空格、换行、制表符
   print('Hello world'.strip('leh'))

"""
输出像列表一样
"""
def printTableLike():
    picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
    print('picnicItems'.center(20,'-'))
    for k,v in picnicItems.items():
        print(k.ljust(14,'.') + str(v).rjust(6))

# 获取数组中元素最大字符串长度
def getMaxLengthOfList(tempList):
    length = 0
    for item in tempList:
        if len(item) > length:
            length = len(item)
    return length

# 输出列表
def printTable():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
    resultList = [''] * 4
    for index in range(len(tableData)):
       tempList = tableData[index]
       tempLength = getMaxLengthOfList(tempList)
       for index1 in range(len(tempList)):
          resultList[index1] += tempList[index1].ljust(tempLength + 5)

    for item in resultList:
       print(item)
           

#printTableLike()   
#handleString()
printTable()
