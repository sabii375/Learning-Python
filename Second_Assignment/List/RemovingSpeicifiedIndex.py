#. Write a python program to print a specified list after removing the 0th, 4th and 5th item. 
# Given list is [“Until”, “I”, “am”,”yours”,”you’re”,”mine”].

def remove_list():
    given_list =  [ "Until", "I", "am", "yours", "you're", "mine"]
    given_list.pop(5)
    given_list.pop(4)
    given_list.pop(0)
    return given_list
result = remove_list()
print(f"The list after removing is {result}")

                