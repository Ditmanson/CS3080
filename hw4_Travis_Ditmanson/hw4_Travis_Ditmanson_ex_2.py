''' 
Homework 4, Exercise 2  
Name Travis Ditmanson
Date 1 March 2023
Copy phone numbers and email addresses from clip board to output
'''

#import files
import pyperclip
import re


def main():
    #import from clipboard
    clipboard=(pyperclip.paste())
    #create phonenumber and email redgex's
    phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
    email_regex = re.compile(r'\w+@\w+\.\w+')
    #save all emails and phone numbers in a list
    emails= email_regex.findall(clipboard)
    phone_numbers = phone_num_regex.findall(clipboard)
    #create some print statments to say whats going on
    print("\n__Phone Numbers__")
    # since we don't know if the phone numbers match to emails i'll print them seperatly
    # since we are printing them seperatly let's use a for loop to number each one
    for i in range(len(phone_numbers)):
        print(f'{i+1} : {phone_numbers[i]}')
    print("\n______Emails_____")
    for i in range(len(emails)):
        print(f'{i+1} : {emails[i]}')
    print()
    return
#some sorta boiler plate statment ive been told is good to include
if __name__ == "__main__":
    main()