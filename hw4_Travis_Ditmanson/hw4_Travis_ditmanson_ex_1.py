''' 
Homework 4, Exercise 1  
Name Travis Ditmanson
Date 1 March 2023
Practice inheritance with basic shape classes
'''
from cmath import pi
import math

#abstract class
class Shape():
    def get_area(self):
        pass
    def get_perimeter(self):
        pass

#rectangle is child of shape and parent of square
class Rectangle (Shape):
    #constructor
    def __init__ (self,width,length):
        self.width = width
        self.length = length
    #area calculator
    def get_area(self):
        return self.width * self.length
    #diagonal calculator
    def get_diagonal(self):
        return math.sqrt(math.pow(self.width,2) + math.pow(self.length,2))
    # perimeter calculator
    def get_perimeter(self):
        return 2*self.length + 2*self.width
# square is a child of the rectangle class
class Square (Rectangle):
    #constructor
    def __init__ (self,width):
        self.width = width
        self.length = width
    #utilizes parents getter functions
#circle is child of shape.
class Circle():
    #circle constructor
    def __init__ (self,radius):
        self.radius = radius
    #I included this so that when grading you can verify results without the debugger
    def get_radius(self):
        return self.radius
    # get_perimeter should be get circumfrence but i used perimeter because of abstract parent class
    def get_perimeter(self):
        return 2*self.radius*pi
    #get area
    def get_area(self):
        return pi*math.pow(self.radius,2)
#circumfrence = 2pir
#r=c/2pi
def main():
    rectangle = Rectangle(10,20) #declare and initilize rectangle
    radius = (((rectangle.get_diagonal()/(4*pi)))) # find radius to make circle
    circle = Circle(radius) # create circle object
    #the rest of this is just so you don't need the debugger to grade
    print(f'rectangle diangle divided by two: {rectangle.get_diagonal()/2}')
    print(f'circle radius: {circle.get_radius()}')
    print(f'circle circum: {circle.get_perimeter()}')

if __name__ == "__main__":
    main()