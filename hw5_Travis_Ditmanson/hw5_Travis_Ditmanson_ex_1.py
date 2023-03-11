''' 
Homework 5, Exercise 1  
Name Travis Ditmanson
Date 11 March 2023
Write  an iterator class reverseIter, that takes a list and iterates it from the revesrse direction.
'''
# reverse iter class
class ReverseIter:
    # constructor
    def __init__(self, list):
        self.list = list
        #set index to end of list
        self.index = len(list)
    # return self, required for iterator classes
    def __iter__(self):
        return self
    #reverse iteration method
    def __next__(self):
        self.index -= 1 # decrement in reverse
        if self.index < 0:
            raise StopIteration
        else:
            return self.list[self.index]
#main method
def main():
    #create test list
    my_list = [1,2,3,4,5,6,7,8,9,]
    #build iterator object
    reverse_iterator = ReverseIter(my_list)
    #print class type for grader to see, just to make your life easier
    print(f'Class type: {type(reverse_iterator)}')
    for value in range(len(my_list)):
        #weird print statment to match output
        print(">>>next(it)")
        #use of reverse iterator
        print (reverse_iterator.__next__())

if __name__ == "__main__":
    main()