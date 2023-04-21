#Write a program to find the sum of digits of a number entered by the user.
def sum_of_digits(num):
    add = 0
    while num!=0:
        digit = num % 10
        num = num // 10
        add = add + digit
    return add
num = int(input("Enter the number form the user: "))
num1 = sum_of_digits(num)
print(f"The sum of digits is { num1}")