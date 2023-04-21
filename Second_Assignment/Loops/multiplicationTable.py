#. Write a program to generate a multiplication table where the number is given by the user.
def mulpiply(n):

    for a in range(1,11):
        print(f"{n} * {a} = {n*a}")
num = int(input("Enter the value from the user: "))
mulpiply(num)