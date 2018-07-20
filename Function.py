
# print函数
def sayHello():
    print('Hello guys')
    print(None)
    print('Hello ', end = '')
    print('world!')

# while循环
def funcitonWihle():
    while True:
        print('-100 的绝对值是' + str(abs(-100)))
        print('Input exit to exit.')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You input ' + response + '.')

# 修改全局变量的值
def modifyGlobalVarivable():
    global username
    username = 'Kevin'

# 捕获异常
def catchException(divide):
    try:
        return 20 / divide
    except ZeroDivisionError:
        print('Error: Divide by Zero')

# 函数调用
import sys
# sayHello()
username = 'Cater'
modifyGlobalVarivable()
print(username)

catchException(0)

