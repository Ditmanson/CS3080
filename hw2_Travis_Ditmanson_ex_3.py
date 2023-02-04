''' 
Homework 2, Exercise 3  
Name Travis Ditmanson
Date 4 Feb 2023
demonstrate basic uses of lists
'''


def strList(array):
    for element in range(len(array)-1): #skil last element in array
        print("%s, " % array[element], end="") #add a comma and remove new line character
    print("and %s" % array[-1]) # all that's left is to print "and" + last element of array
    return array


def main():
    things = ['Wallet', 'Phone', 'Keys'] #initialize things
    things.sort() #sort things
    print(things[0]) #print first element
    print(things[1:3])#print second and third elements
    print(things[-1])#print last element
    print(things.index('Keys'))#print index value where keys are stored
    things.append('Tablet')#add tablet to end of things list
    print(things)
    things.insert(1, 'Mask') #insert mask into index value 2
    print(things)
    things.remove('Phone') #remove phone from list
    print(things)
    things.reverse() #reverse order of list
    print(things)
    strList(things) #i guess this is a toString() for our list


main()
