import math

class shape:
    pass

class rectangle (shape):

    def __init__ (self,width,length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length
    
    def get_diagonal(self):
        return math.sqrt(math.pow(self.width,2) + math.pow(self.length,2))
    
    def get_perimeter(self):
        return 2*self.length + 2*self.width
    


def main():
    p1= rectangle(3,4)
    print(p1.get_perimeter())

if __name__ == "__main__":
    main()