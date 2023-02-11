''' 
Homework 3, Exercise 2  
Name Travis Ditmanson
Date 8 Feb 2023
Count occurances of a character in a string
'''

import pprint
test_string = 'The quick brown fox jumps over the lazy dog.'
counted_characters = {} #empty dictionary
for character in test_string: #for loop length == to test_string
    counted_characters.setdefault(character, 0) # each character in the string is a key and it's default value is zero
    counted_characters[character] = counted_characters[character] + 1 #increment the value in that characters key by 1
pretty_string = pprint.pformat(counted_characters) # format string in alphabetical order
print(pretty_string) #print string
