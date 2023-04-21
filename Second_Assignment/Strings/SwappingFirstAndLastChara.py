#Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def new_string(name):
     
    first_char = name[-1]
    last_char = name[0]
    middle_char = name[1:-1]
    string = first_char + middle_char + last_char
    return string
name = input("Enter the string: ")
result = new_string(name)
print(f"The new string is {result}")

