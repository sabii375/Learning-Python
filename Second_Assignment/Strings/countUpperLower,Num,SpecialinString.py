#Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
def count_characters(name):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
    for each in name:
        if each.isupper():
            count1 += 1
        elif each.islower():
            count2 += 1
        elif each.isdigit():
            count3 += 1
        else:
            count4 += 1
    return count1, count2, count3, count4
name = input("Enter the string: ")
result1, result2, result3, result4 = count_characters(name)
print(f"The numbers of uppercase is {result1}, lowercase is {result2}, special character is {result4} and numeric value is {result3}")