#. Write a Python program to delete all occurrences of a specified character in a given string
def delete(name,specified_character):
    new_string = ""

    for char in name:
        if char != specified_character:
            new_string += char
        
    return new_string
    
name = input("Enter the string: ")
specified_character = input("Enter the specified character to be deleted: ")
result = delete(name,specified_character)
print(f"The string after deleted is {result}")



