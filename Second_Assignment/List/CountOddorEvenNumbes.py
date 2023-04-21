# Write a program to count the number of odd and even numbers in a list.
def odd_even(num):
    count_odd = 0
    count_even = 0
    items = []
    for each in range(num):
        item = int(input("Enter the item of the list: "))
        items.append(item)
    
        if item % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return items, count_odd, count_even         
   
num = int(input("Enter the number of items in list: "))
items, result_odd, resuly_even = odd_even(num)
print(f"The list is {items} total odd numbers is {result_odd} and even numbers is {resuly_even}")
