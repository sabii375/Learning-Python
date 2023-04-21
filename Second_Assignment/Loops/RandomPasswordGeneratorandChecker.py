'''
 Write a function that generates a random password. The password should have a 
random length of between 7 and 10 characters. Each character should be randomly 
selected from positions 33 to 126 in the ASCII table. Your function will not take any 
parameters. It will return the randomly generated password as its only result. Display 
the randomly generated password in your file’s main program. In this exercise you 
will write a function that determines whether or not a password is good. We will 
define a good password to be a one that is at least 8 characters long and contains at 
least one uppercase letter, at least one lowercase letter, and at least one number. Your 
function should return true if the password passed to it as its only parameter is good. 
Otherwise it should return false. Include a main program that reads a password from 
the user and reports whether or not it is good. write a program that generates a random 
good password and displays it. Count and display the number of attempts that were 
needed before a good password was generated.
'''
from random import randint
def random_password():
    password = ""
    length = randint(7,10)

    for n in range(length-1):
        Character_position = randint(33,126)
        random_password = chr(Character_position)
        password = password + random_password
    return password
# Generated_password = random_password()
# print(f"The random generated password is {Generated_password}")

def check(password):
    length = False
    Upper_case = False
    Lower_case = False
    Number = False

    if len(password)>=8:
        length = True
    for each in password:
        if each.isupper():
            Upper_case = True
        elif each.islower():
            Lower_case = True
        elif each.isdigit():
            Number = True
    if length and Upper_case and Lower_case and Number:
        return True
    
    return False
# password = input("Enter the password: ")
# result = check(password)  
# if result:
#     print("The password is good.")

# print("The password is bad.")         
        