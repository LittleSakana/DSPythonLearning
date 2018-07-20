# if-elif-else
name = 'James'
password = 'asdfgh'
if name == 'Kevin':
    print('Hello Kevin');
    if password == 'asdfgh':
        print('Access granted')
    else:
        print('Wrong password')
elif name == 'James':
    print('King！！！！！')

# while
name = ''
while name != 'your name':
    print('Please input your name')
    name = input()
print('Thank you')

# for
for i in range(5):
    print('For loop time (' + str(i) + ')')
for i in range(0, 19, 2):
    print('For loop step time (' + str(i) + ')')
