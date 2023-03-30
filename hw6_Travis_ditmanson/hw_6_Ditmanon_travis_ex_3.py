''' 
Homework 6, Exercise 3 
Name Travis Ditmanson
Date 27 March 2023

Write a Python program to keep track of multiple pieces of text. The program will save each piece
of clipboard text under a keyword. For simplicity you can save this file as mcb.py (mcb stands
for multiclipboard; the shorter name makes it easy if you run it from the command line).

Here’s what the program does:
1. The command line argument is checked.
2. If the argument is ‘save’, then the current clipboard contents are saved under the keyword
after ‘save’.
3. If the argument is ‘list’, then all the saved keywords are printed.
4. Otherwise, if only one keyword is provided and no ‘save’ or ‘list’ is in the arguments, the
text saved under this keyword is copied to the clipboard

'''
import sys
import pyperclip
import shelve

def save_clipboard_text(keyword):
    mcbShelf = shelve.open('mcb') #open the shelf
    mcbShelf[keyword] = pyperclip.paste() #save the clipboard text to the shelf
    mcbShelf.close() #`close the shelf

#following method works by printing the keys to the clipboard

def list_clipboard_text():
    mcbShelf = shelve.open('mcb')
    pyperclip.copy(mcbShelf.keys())
    mcbShelf.close()
def copy_clipboard_text(keyword):
    mcbShelf = shelve.open('mcb')
    if keyword in mcbShelf:
        pyperclip.copy(mcbShelf[keyword])
    mcbShelf.close()

def check_script_arguments():
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == 'save':
            save_clipboard_text(sys.argv[2])
        else:
            print('Invalid command line argument')
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            list_clipboard_text()
        else:
            copy_clipboard_text(sys.argv[1])
    else:
        print('Invalid command line argument')

