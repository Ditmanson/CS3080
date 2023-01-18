import random
import sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:  # Game
    print("%s wins, %s Losses, %s Ties" % (wins, losses, ties))
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    while True:
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'p' or playerMove == 'r' or playerMove == 's':
            break

    if playerMove == 'r':
        print("ROCK versus...")
    elif playerMove == 's':
        print("SCISSORS versus...")
    elif playerMove == 'p':
        print("PAPER versus...")

        # Display what the computer chose:

    randomNumber = random.randint(1, 3)
    computerMove = ''
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")

    if playerMove == computerMove:
        print("It is a tie!")
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win')
        wins += 1
    else:
        print('You lost')
        losses += 1
