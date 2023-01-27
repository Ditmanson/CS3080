import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        """Bagels, a deductive logic game 

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:       That means:
   Pico           one digit is correct but in the wrong position
   Fermi          one digit is correct and in the right position
   Bagels         No digit is correct.

For example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico.""".format(
            NUM_DIGITS
        )
    )

    while True:
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print(" You have {} guesses to get it.".format(MAX_GUESSES))
        # numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secretNum))

        # NEED CODE HERE

        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits"""
    numbers = list("0123456789")  # Create a list of digits 0-9
    # random.shuffle(numbers)  # Shuffle them into random order
    secretNum = " "
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


# NEED CODE HERE


def getClues(guess, secretNum):
    """Returns a string with pico, ermi, bagels clues for a guess and a secret number pair."""
    if guess == secretNum:
        return "You got it!"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit is in the correct place.
            clues.append(guess["Fermi"])
        elif guess[i] in secretNum:
            # a correct  digit is in the incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # there are no correct digits at all.capitalize
    else:
        # sort the clues into the alphabetical order their original order
        # doesn't give any information away.
        clues.sort()
        # make a single string from the list of string clues
        return " ".join(clues)


main()
