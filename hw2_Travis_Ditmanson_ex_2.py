''' 
Homework 2, Exercise 2  
Name Travis Ditmanson
Date 4 Feb 2023
Go through Collatz sequence but validate users integer
'''
#start a collatz number with any number user passes as an argument
def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1
#main function includes the try and exception blocks
def main():
    print("Enter number: ")
    number = input()
    while number != 1:
        try:
            number = collatz(int(number))
            print(number)
        except: #will repeat until user passes an integer
            print("Integers only please!")
            number = input()

main()
