# Write a program to find the reverse of the number entered by the user.
def reverse_number(num):
    reverse = 0
    while num!=0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse
# num = int(input("Enter the number: "))
# num1 = reverse_number(num)
# print(f"The reverse of the given number is {num1}")

