#冰雹猜想实现

def collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
    else:
        result = number * 3 + 1
        
    print(str(result))
    return result

def collatzSequence():
    print('Please input a number!')
    try:
        inputNumber = int(input())
        temp = collatz(inputNumber)
        while temp != 1:
            temp = collatz(temp)
            
    except ValueError:
        print('Invalid type, Please re-enter a number!')
        collatzSequence()

collatzSequence()
