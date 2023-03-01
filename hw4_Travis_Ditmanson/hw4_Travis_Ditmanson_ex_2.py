''' 
Homework 4, Exercise 2  
Name Travis Ditmanson
Date 1 March 2023
Copy phone numbers and email addresses from clip board to output
'''

import pyperclip
import re


def main():
    clipboard=(pyperclip.paste())
    phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
    email_regex = re.compile(r'\w+@\w+\.\w+')
    emails= email_regex.findall(clipboard)
    phone_numbers = phone_num_regex.findall(clipboard)
    print("\n__Phone Numbers__")
    for i in range(len(phone_numbers)):
        print(f'{i+1} : {phone_numbers[i]}')
    print("\n______Emails_____")
    for i in range(len(emails)):
        print(f'{i+1} : {emails[i]}')
    print()



    return

if __name__ == "__main__":
    main()