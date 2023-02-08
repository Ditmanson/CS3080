''' 
Homework 3, Exercise 1  
Name Travis Ditmanson
Date 8 Feb 2023
iterate through a list of lists, column by column
'''

#list of lists grid
grid =\
[['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


for column in range(len(grid[0])): #outer for loop increments once for each column
    for row in range (len(grid)): #inner for loop increments once for each row
        print(grid[row][column],end='')
    print() #prints new line character
