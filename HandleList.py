# 数组操作

def handleList():
    spam = ['cat', 'bat', 'Rat', 'elephant']
    print(spam[0:4]) # ['cat', 'bat', 'rat', 'elephant']
    print(spam[1:3]) # ['bat', 'rat']
    print(spam[0:-1]) # ['cat', 'bat', 'rat']
    print('cat' not in spam) # False 判断元素是否在数组中
    print('bat' in spam) # True
    del spam[2] # 删除数组的第二个元素
    print(spam)
    spam.append('dog')
    spam.insert(1, 'Tiger')
    print(spam)
    spam.sort() # 根据ASCII码进行排序
    print(spam)
    spam.sort(reverse = True) # 倒序
    print(spam)
    spam.sort(key = str.lower) # 根据字母表顺序排序
    print(spam)
    spam.sort(key = str.lower, reverse = True) # 按字母表顺序倒序
    print(spam)
    
    index = spam.index('bat') # 1
    print('Index of bat is ' + str(index))


def listFunction(param):
    mylist = ['1', '2', '3', '4', '5']
    try:
        temp = mylist.index(param)
        print('Index of ' + param + ' is ' + str(temp))
    except ValueError:
        print(param + '不在数组中')

def transfer():
    mylist = ['1', '2', '3', '4', '5']
    # 把数组转化成元组
    myTuple = tuple(mylist)
    print(myTuple)

    # 把元组转化成数组
    temp = list(myTuple)
    print(temp)





# 数组基本操作
handleList()

# 数组和元组相互转化
transfer()

# 判断是否在数组中
print('Please input a number')
inputValue = input()
listFunction(inputValue)

