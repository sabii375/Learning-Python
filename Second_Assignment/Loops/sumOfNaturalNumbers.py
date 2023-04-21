#Write a program to find the sum of first n natural numbers.
num = int(input("Enter the value of n:"))
sum = 0
for n in num:
    sum = sum + n
print(f"The sum of first n natural number is: {sum}")
