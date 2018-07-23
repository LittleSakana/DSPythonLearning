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

getAgeWithName()
            
