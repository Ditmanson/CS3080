'''

Homework 6, Exercise 2 
Name Travis Ditmanson
Date 27 March 2023

The famous Fibonacci Sequence is the series of numbers like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers prior to it.
- 2 is found by adding the two numbers before it (1+1)
- 3 is found by adding the two numbers before it (1+2),
- 5 is (2+3),
- ……
An implementation could be like this:
def fibonacci(num):
 if num < 2:
 return num
 return fibonacci(num - 1) + fibonacci(num - 2)
But the runtime performance is terrible. This is because the code keeps recalculating Fibonacci
numbers that are already known.
1. Implement a @cache decorator that will save the calculations in a function attribute
dictionary. Even though the function fibonacci(num) only has one input argument,
please make the decorator work for functions with any number of arguments (the
decorator’s own arguments can be ignored).
2. Apply the @countCalls decorator introduced in class to the fibonacci function. Do you
see a difference between using @cache and not using it (hint: use nested decorator)?
Write your conclusion at the top of your code, in the multiline comment under
“Description of your program”.
3. Save your code as hw6_firstname_lastname_ex_2.py

'''
import functools

def cache(func):
    @functools.wraps(func) #this is a decorator that will preserve the metadata of the function
    def wrapper_cache(*args, **kwargs): #this is the wrapper function
        cache_key = args + tuple(kwargs.items()) #this is the key for the cache dictionary
        if cache_key not in wrapper_cache.cache: #if the key is not in the cache dictionary
            wrapper_cache.cache[cache_key] = func(*args, **kwargs) #add the key and the value to the cache dictionary
        return wrapper_cache.cache[cache_key] #return the key
    wrapper_cache.cache = {} #create the cache dictionary
    return wrapper_cache #return the wrapper function

#countcalls from class
def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)
    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

@countCalls
@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    num = 2
    print(f"Fibonacci({num}) = {fibonacci(num)}")
    print(f"Number of function calls: {fibonacci.numCalls}")

if __name__ == "__main__":
    main()

