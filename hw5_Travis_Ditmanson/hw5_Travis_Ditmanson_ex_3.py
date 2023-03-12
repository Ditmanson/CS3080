''' 
Homework 5, Exercise 3  
Name Travis Ditmanson
Date 11 March 2023
The range() function creates a sequence. For very large sequences, this consumes a lot of memory. 
You can write a version of range() which does not create the entire sequence, but instead yields 
the individual values. Using a generator will have the same effect as iterating through a sequence 
but won’t consume as much memory.
'''
import math
'''Define a generator called genrange(), which generates the same sequence of values as range(), without creating a list object'''
#set defaults in the parameters
def genrange(stop, start=0, step=1):
    try:
        for x in range(start, stop, step):
            yield x
    except:
        pass
def main():
    test_range_one=genrange(5)
    test_range_two=genrange(10,5)
    test_range_three=genrange(20,10,2)
    print("Output with one parameter: 5 stop ")
    for x in test_range_one:
        print(x)
    print("Output with two parameters: 10 stop 5 start ")
    for x in test_range_two:
        print(x)
    print("Output with three parameters: 20 stop, 10 start, 2 step ")

    for x in test_range_three:
        print(x)

if __name__ == "__main__":
    main()