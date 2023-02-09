
TicTacToe = {'topLeft': ' ', 'topRight': ' ', 'topCenter': ' ',\
            'centerLeft': ' ', 'centerCenter': 'x ', 'centerRight': ' ',\
            'bottomLeft': ' ', 'bottomCenter': ' ', 'bottomRight': ' ', }


def printBoard(board):
    marks = list(board.values())
    print("{:<2} {:<2} {:<2}".format(str(TicTacToe.get('topLeft')+' |'),
            str(TicTacToe.get('topCenter')+' |'), str(TicTacToe.get('topRight'))))
    print("---------")
    print("{:<2} {:<2} {:<2}".format(str(TicTacToe.get('centerLeft')+' |'),
            str(TicTacToe.get('centerCenter')+' |'), str(TicTacToe.get('centerRight'))))
    print("---------")
    print("{:<2} {:<2} {:<2}".format(str(TicTacToe.get('bottomLeft')+' |'),
            str(TicTacToe.get('bottomCenter')+' |'), str(TicTacToe.get('bottomRight'))))


def move(board, turn):
    if turn % 2 == 0:
        print("It is X's turn")
    else:
        print("It is O's turn")
    move = 'a'
    while move not in board.keys() or board[move]!= ' ':
        print("Where would you like to move?")
        print('topLeft, topCenter, topRight')
        print('centerLeft, centerCenter, centerRight')
        print('bottomLeft, bottomCenter, bottomRight')
        move = input()
    if turn % 2 == 0:
        board[move]='X'
    else:
        board[move]='O'

def gameOn():
    gameOver = False
    turn = 0
    while gameOver==False:
        printBoard(TicTacToe)
        move(TicTacToe, turn)
        turn=+1


gameOn()
printBoard(TicTacToe)
