
from re import A
from unicodedata import decimal


# def hexToDecimal(hexadecimal):
#     lengthOfHex = len(hexadecimal)
#     characters = list(hexadecimal)
#     sum = 0
#     for i in characters:
#         print(characters[i])
#         # if characters[i] == 'A':
#         #     characters[i] = ('10')
#         # elif characters[i] == 'B':
#         #     characters[i] = ('11')
#         # elif characters[i] == 'C':
#         #     characters[i] = ('12')
#         # elif characters[i] == 'D':
#         #     characters[i] = ('13')
#         # elif characters[i] == 'E':
#         #     characters[i] = ('14')
#         # elif characters[i] == 'F':
#         #     characters[i] = ('15')
#         # sum += (int(characters[i])*16**lengthOfHex)
#         # lengthOfHex -= 1
#         return "sum"
def hexToDecimal(hexadecimal):
    lengthOfHex = len(hexadecimal)
    characters = list(hexadecimal)
    sum = 0
    for i, c in enumerate(characters):
        sum += int(c, 16)*(16**(lengthOfHex-i-1))
    return sum


print(hexToDecimal('ABC'))


def hexFromDecimal(decimal):
    decimalDigit1 = decimal % 16
    decimal = int(decimal/16)
    decimalDigit2 = decimal % 16
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
