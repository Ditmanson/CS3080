''' 
Homework 3, Exercise 3  
Name Travis Ditmanson
Date 8 Feb 2023
Program uses a dictionary to create a working inventory of items
'''

inventory = {'Hand sanitizer': 10, 'Soap': 6, 'Kleenex':22, 'Lotion':16 , 'Razors': 12}

def printInventory(inventory): #inventory uses the .items() function from lecutre
    for i, j in inventory.items():
        print("{:<15} {:<10}".format(str(i)+":", str(j))) 
        #formated the string to make get the numbers to align. Might not work if we get an item longer than hand sanitizer

def addItem(inventory, item): #function sets default to 0 if then increments
    inventory.setdefault(item, 0)
    inventory[item] +=  + 1

def deleteItem(inventory, item):#item decrements if inventory is larger than 0
    if inventory[item] != 0:
        inventory[item] -= 1
    else:
        print("Item cannot be deleted any further")
