''' 
Homework 2, Exercise 1  
Name Travis Ditmanson
Date 4 Feb 2023
Go through Collatz sequence
'''
#collatz sequence is incomplete if not used in a while loop
def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1

def main():
    print("Enter number: ")
    number = int(input()) #will return error if integer is not passed
    while number != 1: #utilzied in a while loop in seperate function for readability
        number = collatz(number)
        print(number)

main()