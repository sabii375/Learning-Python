#Write a Python program to swap cases in a given string. Example: pYTHON eXERCISEdef 
def swap_case(name):
    case_swap = " "

    for char in name:
        if char.isupper():
            case_swap += char.lower()
        elif char.islower():
            case_swap += char.upper()
        else:
            case_swap += char
    return case_swap
name = input("Enter the string: ")
result = swap_case(name)
print(f"The swapped string is {result}")

