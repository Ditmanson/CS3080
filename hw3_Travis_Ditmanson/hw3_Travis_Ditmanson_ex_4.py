''' 
Homework 3, Exercise 4  
Name Travis Ditmanson
Date 10 Feb 2023
iterate through a list of lists, column by column
'''
#create board with dictionary
TicTacToe = {'topLeft': ' ', 'topRight': ' ', 'topCenter': ' ',\
            'centerLeft': ' ', 'centerCenter': ' ', 'centerRight': ' ',\
            'bottomLeft': ' ', 'bottomCenter': ' ', 'bottomRight': ' ', }

#print board using formated print strings
def printBoard(board):
    print("{:<2} {:<2} {:<2}".format(str(board.get('topLeft')+' |'),
            str(board.get('topCenter')+' |'), str(board.get('topRight'))))
    print("--+---+--")
    print("{:<2} {:<2} {:<2}".format(str(board.get('centerLeft')+' |'),
            str(board.get('centerCenter')+' |'), str(board.get('centerRight'))))
    print("--+---+--")
    print("{:<2} {:<2} {:<2}".format(str(board.get('bottomLeft')+' |'),
            str(board.get('bottomCenter')+' |'), str(board.get('bottomRight'))))

#method for taking a turn
def move(board, turn):
    if turn % 2 == 0: # every other turn switch players
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
        move = input() #continue till user picks an appropriate square
    if turn % 2 == 0: #how we decide to put an x or an o in the block
        board[move]='X'
    else:
        board[move]='O'

def gameOn(board):
    turn = 0 #increment turns to decide who's turn it is and to decide when its a cats game
    gameOver = False
    while gameOver==False:#continue till boolean changes
        move(TicTacToe, turn)
        if turn >=8: # first check if the game is a tie
            gameOver = True
            print("\nCats Game, no winner")
            #all elif statments are to check for a winner
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
        turn+=1#increment turn after a move has been played and game is not over
        

gameOn(TicTacToe)
print()
printBoard(TicTacToe)
print()
