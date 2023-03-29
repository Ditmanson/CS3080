''' 
Homework 6, Exercise 1  
Name Travis Ditmanson
Date 27 March 2023
Write a @slowDown decorator that will sleep for a certain number of seconds before it calls the
decorated function. Use an optional rate argument for the decorator that controls how long (in
seconds) it sleeps. Use a default value of 1 second for the sleep duration.

Note that you can modify the @slowDown example provided in class by letting the decorator
accept an optional argument that is the number of seconds to sleep, and then use the same
recursive countdown(fromNumber) as the function to decorate and test the decorator
'''
import functools
import time
#"""Sleep 1 second before calling the function"""

def slowDown(rate=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapperSlowDown
    return decorator
        

@slowDown(rate=2)
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)


# def slowDown(rate=1):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             time.sleep(rate)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

def main():
    countdown(5)

if __name__ == "__main__":
    main()