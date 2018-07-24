# 九宫格模拟下棋

theBoard = {'11':' ', '12':' ', '13':' ',
            '21':' ', '22':' ', '23':' ',
            '31':' ', '32':' ', '33':' '}
def printBoard():
    print(theBoard['11'] + '|' + theBoard['12'] + '|' + theBoard['13'])
    print('-----')
    print(theBoard['21'] + '|' + theBoard['22'] + '|' + theBoard['23'])
    print('-----')
    print(theBoard['31'] + '|' + theBoard['32'] + '|' + theBoard['33'])

def ticTacToe():
    turn = 'X'
    for i in range(9):
        printBoard()
        print('It\'s ' + turn + '\'s turn, move to which space?')
        move = input()
        if move == '':
            break
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    printBoard()

ticTacToe()
