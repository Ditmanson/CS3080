''' 
Homework 2, Exercise 4 part 1  
Name Travis Ditmanson
Date 4 Feb 2023
Guessing game returns higher or lower based on users guess of seceret number
'''
import random
#constants for readability
TRIES = 10 
LOWER = 1
UPPER = 20

def guess_number():
    secret_number = random.randint(LOWER,UPPER)
    print("I am thinking of a number between %d and %d. You have %d tries." %(LOWER ,UPPER ,TRIES))
    return secret_number

def guessing_game(secret_number):
    for i in range(TRIES):
        while True:
            try:
                number = int(input())
                break
            except:
                print("guess a number!")
        if number == (secret_number):
            print("Good Job! You guessed my number in %d guesses!" %(i+1)) #turns out the first time through is try zero
            return
        elif number>secret_number:
            print ("Your guess is too high")
        elif number<secret_number:
            print("Your guess is too low.")
        
def main():
    secret_Number = guess_number()
    guessing_game(secret_Number)

main()


