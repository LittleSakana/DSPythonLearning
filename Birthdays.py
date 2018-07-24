# 输入名字，返回年龄

def getAgeWithName():
    birthdays = {'James':18, 'Alice':30, 'Chris':24, 'Kevin':49}
    while True:
        print('Please input a name:')
        name = input()

        if name == '':
            break

        if name in birthdays:
            print(name + '\'s age is ' + str(birthdays[name]))
        else:
            print(name + ' is not exist.')
            print('What\'s ' + name + ' age?')
            try:
                age = int(input())
            except ValueError:
                print('Error Age!')
                continue
            birthdays[name] = age
            print('Birthday database updated!')

# 获取字符串中字符出现的次数
import pprint
def countCharacter():
    message = 'The setdefault() method is a nice shortcut to ensure that a key exists. Here is a short program that counts the number of occurrences of each letter in a string. Open the file editor window and enter the following code, saving it as characterCount.py:'
    count = {}
    for character in message:
        count.setdefault(character,0)
        count[character] += 1
    # Pretty Print 完美输出
    #pprint.pprint(count)
    print(pprint.pformat(count))

#getAgeWithName()
countCharacter()
            
