
# Write a program to count the number of digits in a number. 

def digits(num):
    count = 0
    while num!=0:
        di = num % 10
        num = num // 10
        count = count + 1
    return count
num = int(input("Enter any number: "))
num1 = digits(num)
print(f"The number of digits is {num1}")