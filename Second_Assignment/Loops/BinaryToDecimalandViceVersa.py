#. Write a program to converts binary to decimal and vice versa. Let the user choose which operation to perform
def binary_to_decimal_conversion():
    num = int(input("Enter the binary value: "))
    power = 0
    result = 0
    while num!=0:
        digit = num % 10
        result = result + digit * (2 ** power)
        power = power + 1
        num = num // 10
    print(f"The decimal of given binary is : {result}")

def decimal_to_binary_conversion():
    num = int(input("Enter the decimal value: "))
    dec = ""

    while num!=0:
        digit = num % 2
        dec = dec + str(digit)
        num = num // 2
    
    result =  dec[::-1]
    print(f"The binary of the given decimal is : {result}")

print("1: Binary to Decimal \n2: Decimal to Binary")
choice = input("Enter your choice: ")
if choice == 1:
    binary_to_decimal_conversion()
else:
    decimal_to_binary_conversion()




