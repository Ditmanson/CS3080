TicTacToe = {'topLeft': ' ', 'topRight': ' ', 'topCenter': ' ',\
            'centerLeft': ' ', 'centerCenter': ' ', 'centerRight': ' ',\
            'bottomLeft': ' ', 'bottomCenter': ' ', 'bottomRight': ' ', }


def printBoard(board):
    print("{:<2} {:<2} {:<2}".format(str(board.get('topLeft')+' |'),
            str(board.get('topCenter')+' |'), str(board.get('topRight'))))
    print("--+---+--")
    print("{:<2} {:<2} {:<2}".format(str(board.get('centerLeft')+' |'),
            str(board.get('centerCenter')+' |'), str(board.get('centerRight'))))
    print("--+---+--")
    print("{:<2} {:<2} {:<2}".format(str(board.get('bottomLeft')+' |'),
            str(board.get('bottomCenter')+' |'), str(board.get('bottomRight'))))


def move(board, turn):
    if turn % 2 == 0:
        print("It is X's turn")
    else:
        print("It is O's turn")
    move = 'a'
    while move not in board.keys() or board[move]!= ' ':
        printBoard(board)
        print("Where would you like to move?")
        print('topLeft, topCenter, topRight')
        print('centerLeft, centerCenter, centerRight')
        print('bottomLeft, bottomCenter, bottomRight')
        move = input()
    if turn % 2 == 0:
        board[move]='X'
    else:
        board[move]='O'

def gameOn(board):
    turn = 0
    gameOver = False
    while gameOver==False:
        move(TicTacToe, turn)
        if turn >=8:
            gameOver = True
            print("\nCats Game, no winner")
        elif str(board.get('topCenter')) == str(board.get('topLeft')) == str(board.get('topRight')) and str(board.get('topCenter'))!= ' ':
            gameOver = True
            winner = str(board.get('topCenter'))
            print(f'\n{winner} is the winner')
        elif str(board.get('bottomCenter')) == str(board.get('bottomLeft')) == str(board.get('bottomRight')) and str(board.get('bottomCenter'))!= ' ':
            gameOver = True
            winner = str(board.get('bottomCenter'))
            print(f'\n{winner} is the winner')
        elif str(board.get('centerCenter')) == str(board.get('centerLeft')) == str(board.get('centerRight')) and str(board.get('centerCenter'))!= ' ':
            gameOver = True
            winner = str(board.get('centerCenter'))
            print(f'\n{winner} is the winner')
        elif str(board.get('topLeft')) == str(board.get('bottomLeft')) == str(board.get('centerLeft')) and str(board.get('centerLeft'))!= ' ':
            gameOver = True
            winner = str(board.get('topLeft'))
            print(f'\n{winner} is the winner')
        elif str(board.get('topCenter')) == str(board.get('bottomCenter')) == str(board.get('centerCenter')) and str(board.get('centerCenter'))!= ' ':
            gameOver = True
            winner = str(board.get('topCenter'))
            print(f'\n{winner} is the winner')
        elif str(board.get('topRight')) == str(board.get('bottomRight')) == str(board.get('centerRight')) and str(board.get('centerRight'))!= ' ':
            gameOver = True
            winner = str(board.get('topRight'))
            print(f'\n{winner} is the winner')
        elif str(board.get('topRight')) == str(board.get('centerCenter')) == str(board.get('bottomLeft')) and str(board.get('bottomLeft'))!= ' ':
            gameOver = True
            winner = str(board.get('bottomLeft'))
            print(f'\n{winner} is the winner')
        elif str(board.get('topLeft')) == str(board.get('centerCenter')) == str(board.get('bottomRight')) and str(board.get('bottomRight'))!= ' ':
            gameOver = True
            winner = str(board.get('bottomRight'))
            print(f'\n{winner} is the winner')
        turn+=1
        

gameOn(TicTacToe)
print()
printBoard(TicTacToe)
print()
