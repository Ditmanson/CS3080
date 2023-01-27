import random
import time
import sys


def hi():
    print("Hi!")
    print("Hello!")
    print("how are you?")


def hello(name):  # say hello and name
    print("Hello, " + name)


# comment
<<<<<<< HEAD
'''also comment'''
=======
"""also comment"""
>>>>>>> d9a22a9ffdb09adaf13ca614a708af2b642556bf


def magic8ball(number):
    if number == 1:
        return "It is certain"
    elif number == 2:
        return "It is decidingly so"
    elif number == 3:
        return "Yes"
    elif number == 4:
        return "yeah sure"
    elif number == 5:
        return "not so sure about that"
    elif number == 6:
        return "ask again"
    elif number == 7:
        return "not likely"
    elif number == 8:
        return "lets say no"
    elif number == 9:
        return "naw dawg"
    print("pass a number!")


def zigzag():
    indent = 0
    indentIncreasing = True
    try:
        while True:
            print(" " * indent, end="")
            print("****")
            time.sleep(0.1)
            if indentIncreasing:
                indent += 1
                if indent == 20:
                    indentIncreasing = False
            else:
                indent -= 1
                if indent == 0:
                    indentIncreasing = True
    except KeyboardInterrupt:
        sys.exit()


def main():
    name = "travis"
    hello(name)
    randomNumber = random.randint(1, 9)
    print(magic8ball(randomNumber))
    zigzag()


main()
