#Write a program to reverse a given string without using inbuilt function
def reverse_string(name):
    reverse = ""
    length = len(name)
    for char in name:
        reverse += name[length-1]
        length -= 1
    # for char in range(length - 1, -1, -1):
    #     reverse += name[char]
    return reverse
# name = input("Enter the string: ")
# result = reverse_string(name)
# print(f"The reversed string is {result}")

