#. Write a Python program to sum all the items in a list.
def sum_of_items(n):
    items = []
    summ = 0

    for each in range(n):
        num = int(input("Enter the numbers for the list: "))
        items.append(num)
        summ = summ + num
    return items, summ

n = int(input("Enter the number of items in list: "))
result, add = sum_of_items(n)
print(f"The list is {result} and the sum is {add}")



