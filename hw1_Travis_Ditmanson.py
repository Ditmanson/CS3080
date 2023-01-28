'''
Homework 1
Name: Ditmanson Travis
Date: 01-20-2023
Security Program with Mathy questions'''
import random
from re import A

'''
This security Program uses super nerdy math/computer science questions to move the program along. I will admit that I'm not an expert 
in these conversions and was kind of using this assignment to help study for another class. To make sure my math doesn't stop the grader from
getting to the end of the program, I made a series of hints that end with the correct thing to put in. camelcase is used for naming because that's 
what i've gotten used to in java classes.
'''


'''hexToreturn takes a random binary number and converts it to a hexadecimal string'''


def hexToReturn(binary):
    if binary == '0000':  # the first if statement
        return '0'
    elif binary == '0001':  # the first elif statment
        return '1'
    elif binary == '0010':
        return '2'
    elif binary == '0011':
        return '3'
    elif binary == '0100':
        return '4'
    elif binary == '0101':
        return '5'
    elif binary == '0110':
        return '6'
    elif binary == '0111':
        return '7'
    elif binary == '1000':
        return '8'
    elif binary == '1001':
        return '9'
    elif binary == '1010':
        return 'A'
    elif binary == '1011':
        return 'B'
    elif binary == '1100':
        return 'C'
    elif binary == '1101':
        return 'D'
    elif binary == '1110':
        return 'E'
    elif binary == '1111':
        return 'F'
    else:  # the first else statment
        return 'bad return'  # this should never run


'''findHexFromBinary function is the little math game given to the user, the user has to enter the correct hexadecimal representation of the binary to continue
after 4 tries the answer is given'''


def findHexFromBinary(binary, hexdecimal):
    isCorrect = False  # The first truthy falsey value
    tries = 0
    while isCorrect == False:
        print("What is the hexadecimal value of " + str(binary))
        # first input() and first str(). All comparisions are done with strings
        usersMath = str(input())
        if usersMath == hexdecimal:  # checks if the users conversion matches the programs
            isCorrect = True
        else:
            print("sorry that's not right")
            tries += 1  # here's the first math operator
        if tries == 1:
            print("If your etnering a letter can you capitalize it")
        if tries == 2:
            print("are you sure your math is correct")
        if tries == 3:
            print("Maybe it's not you... maybe it's me ")
        if tries > 3:
            print("Hint it's " + hexdecimal)
    return "Way to go"


'''
this table just prints off the important part of a decimal to hexadecimal table. I use it as a hint in the main code
'''


def printDecimalToHex():
    for i in range(10):  # this is the first range for loop. I wasn't sure if this counted so don't worry, there's another one in main
        print(str(i) + "=" + str(i))  # more str()
    print("10 = A")
    print("11 = B")
    print("12 = C")
    print("13 = D")
    print("14 = E")
    print("15 = F")


'''hex from decimal is an incomplete function that works for the sake of this code. It will take a decimal and translate it into hexadecimal.
I say this is incomplete because it only works for a two digit hexadecimal and i ensured the program only recieves two digit hexadecimals. I think
this is a situation for a recursive function, but at this time, i haven't come up with a way to work for any size of hexadec'''


def hexFromDecimal(decimal):
    decimalDigit1 = decimal % 16  # here's the first modulous math operator
    decimal = int(decimal/16)  # here's some int division
    decimalDigit2 = decimal % 16  # here's another modulus math operator
    if decimalDigit1 == 10:
        decimalDigit1 = 'A'
    elif decimalDigit1 == 11:
        decimalDigit1 = 'B'
    elif decimalDigit1 == 12:
        decimalDigit1 = 'C'
    elif decimalDigit1 == 13:
        decimalDigit1 = 'D'
    elif decimalDigit1 == 14:
        decimalDigit1 = 'E'
    elif decimalDigit1 == '15':
        decimalDigit1 = 'F'
    if decimalDigit2 == 10:
        decimalDigit2 = 'A'
    elif decimalDigit2 == 11:
        decimalDigit2 = 'B'
    elif decimalDigit2 == 12:
        decimalDigit2 = 'C'
    elif decimalDigit2 == 13:
        decimalDigit2 = 'D'
    elif decimalDigit2 == 14:
        decimalDigit2 = 'E'
    elif decimalDigit2 == '15':
        decimalDigit2 = 'F'
    hexadecimal = (str(decimalDigit2) + str(decimalDigit1))
    return hexadecimal


'''createRandomBinary() creates a 4 bit random binary string'''


def createRandomBinary():
    # this is the first random.randit, I used it 4 times here. I use it later too so if this dont count don't worry.
    onesPlace = random.randint(0, 1)
    tensPlace = random.randint(0, 1)
    hundredsPlace = random.randint(0, 1)
    thousandsPlace = random.randint(0, 1)
    return str(onesPlace) + str(tensPlace) + \
        str(thousandsPlace) + str(thousandsPlace)


'''findHexFromDecimal() is the function that is where the user has to convert a hex number from a decimal number'''


def findHexFromDecimal(decimal, hexadecimal):
    tries = 0
    while True:  # another truthy/falsy also another while loop
        usersHexadecimal = str(input())  # another str() and input()
        if usersHexadecimal == str(hexadecimal):  # another str()
            print("that's correct actually")  # the first print stamtement
            break  # the first break statement
        elif tries == 0:  # I'm going to stop counting all the if/elif statments there's more than enough
            print("start by dividing the decimal by 16 and finding the remainder")
        elif tries == 1:
            print("Dividing by 16 gets you " + str(int(decimal/16)))
            print("With a remainder of " + str(decimal % 16))
            print("your remainder is gonna go in the ones place, you need to divide your quotient by 16 again for the tens place")
        elif tries == 2:
            print("look... if it your number was 25...")
            print("25/16 = 1 with a remainder of 9 and 1/16 = 0 with a remainder of 1")
        elif tries == 3:
            print("Check your math with this decimal to hex conversion table")
            printDecimalToHex()
        else:
            print("my math shows decimal: " + str(decimal) +
                  " to hex is: " + hexFromDecimal(decimal))
        tries += 1


'''I couldn't come up with something with my theme. so this function is used to satsify the float requirement'''


def nameDividedBy10(name):
    length = len(name)  # len() function used
    return length/10  # returns a float


'''Main where the magic happens'''


def main():
    # create a random integer that will be our binary number
    binary = createRandomBinary()
    hexadecimal1 = hexToReturn(binary)
    decimal = random.randint(17, 30)
    hexadecimal2 = hexFromDecimal(decimal)
    for i in range(10):  # this is to satisfy the main loop to ask three questions using the range function
        if i % 3 != 0:
            # I know I'm not super clever about why to put a continue in the loop, This is just me checking a box...
            continue
        elif i == 3:  # i would never write a real program this way
            print(findHexFromBinary(binary, hexadecimal1))
        elif i == 6:
            print("ok smart guy let's convert " +
                  str(decimal) + " to hexadecimal")
            print("It's ok i'll help you if you cant figure it out")
            findHexFromDecimal(decimal, hexadecimal2)
        elif i == 9:
            print("i can't think of anything clever for floats and lengths that allows me to keep studying assembly")
            print("whats your name")
            name = input()
            if len(name) % 10 != 0:
                print("The length of your name divided by 10 = " +
                      str(nameDividedBy10(name)))
        print("Binary value: " + str(binary) +
              " \tDecimal value: " + str(decimal))  # well we need something to skip over... also a reminder of the decimal and hexadecimal values is nice


# So I made it this way because of CS 1450 and CS 1150. It feels wrong here though..
main()
