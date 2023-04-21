'''
 A string is a palindrome if it is identical forward and backward. For example “anna”, 
“civic”, “level” and “hannah” are all examples of palindromic words.Write a program 
that reads a string from the user and uses a loop to determines whether or not it is a 
palindrome. Display the result, including a meaningful output message.
'''
from eight import reverse_string
def palindrome(name):
    name1 = reverse_string(name)
    if name == name1:
        print("The string is palindrom.")
    else:
        print("The string is not plaindrome.")
name = input("Enter the string: ")
palindrome(name)

 
