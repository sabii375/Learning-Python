# Write a program to count the number of vowels and consonants in a given string by user. 
def count_number_of_vowel_consonant(name):
    count1 = 0
    count2 = 0
    vowels = "aeiouAEIOU"

    for each in name:
        if each in vowels:
            count1 += 1
        else:
            count2 += 1
    return count1 , count2
name = input("Enter the string: ")
result1, result2 = count_number_of_vowel_consonant(name)
print(f"The number of vowels is {result1} and the number of condonant is {result2}")            