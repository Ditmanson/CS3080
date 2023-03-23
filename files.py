# Ask the user to eneter 1, 2, or 3. If they select anything other than 1, 2, or 3 it should display a suitable error message.

# If they select 1, ask the user to eneter a school subject and save it to a new file called "Subject.txt". It should overwrite any exiting file with a new file.

# If they select 2, display the contents of the "Subject.txt" file.

# If they select 3, ask the user to enter a new subject and save it to the file and then display the entire contents of the file.

def main():
    
    integer=int(input("Enter a 1, 2, or 3\n"))
    if integer == 1:
        school_subject=input("please enter a school subject\n")
        file = open('Subject.txt' , 'wt')
        file.write(school_subject)
    elif integer ==2:
        file = open('Subject.txt', 'r')
        print(file.read())
    elif integer ==3:
        file = open("Subject.txt", 'a')
        new_subject=input("Enter a new subject")
        file.write(f'\n{new_subject}')
    else:
        print("error return code 1")
        return
    

if __name__ == "__main__":
    main()