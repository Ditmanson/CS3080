''' 
Homework 4, Exercise 3  
Name Travis Ditmanson
Date 1 March 2023
Write  a  program  that  uses  regular  expressions  to  make  sure  the  password  string  it  receives 
through an input argument is strong. A strong password in this exercise is defined as one that 
(1) is at least eight characters long, 
(2) contains both uppercase and lowercase characters 
(3)has at least one digit. You may assume there is no other special characters such as punctuations.
'''
import re 

#constant for print statments
STRONG_PASSWORD = ["(1) is at least eight characters long",
                "(2) contains both uppercase and lowercase characters","(3)has at least one digit."]

# use of registers to return false if anything isn't found
def strong_password_checker(password):
    if not re.search(r'[a-z]',password):
        print("must include a lower case character")
        return False
    if not re.search(r'[A-Z]', password):
        print("must include a uppercase character")
        return False
    if not re.search(r'[0-9]', password):
        print("must include atleast one digit")
        return False
    if not re.search(r'\W', password):
        print("must include atleast one special character")
        return False
    if len(password) < 8:
        print("must be atleast 8 charcters long")
        return False
    print("Strong password")
    return True

def main():
    #set defualt to false
    strong_password = False
    #loop till correct
    while not strong_password:
        print("Enter password a strong password")
        #for loop here is just going through password options, used constant for extendability
        for i in range(len(STRONG_PASSWORD)):
            print(STRONG_PASSWORD[i])
        password =input()
        strong_password = strong_password_checker(password)

    return

if __name__ == "__main__":
    main()