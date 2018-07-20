# 这是一个猜数字的游戏

import random
def guessNumber():
    print('I am thinking of a number between 1 and 30')
    fixNumber = random.randint(1, 30)
    count = 0
    while(True):
        count = count + 1
        print('Take a guess.')
        current = input()
        if (int(current) == fixNumber):
            print('Good job! You guessed my number in ' + str(count) + ' guesses!')
            break
        elif (int(current) > fixNumber):
            print('Your guess is too high.')
        else:
            print('Your guess is too low.')


guessNumber()        
