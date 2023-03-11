''' 
Homework 5, Exercise 2  
Name Travis Ditmanson
Date 11 March 2023
Use a generator function or generator experssion to find first n pythagorean triplets, where n is an integer.
A pythagorean triplet is one where x^2 + y^2 = z^2 and none of the integers are zero
'''
import math

def pythagorean_triplets(n):
    #seq = iter(seq)
    #result = []
    try:
        for x in range(1, n+1):
            for y in range(x, n+1):
                for z in range(y, n+1):
                    if math.pow(x,2) + math.pow(y,2) == math.pow(z,2):
                        yield (x,y,z)
    except:
        pass 
            


def main():
    print("Starting")
    pythagorean_triplet=pythagorean_triplets(69)
    for triplet in pythagorean_triplet:
        print(triplet)

if __name__ == "__main__":
    main()