#Write a python program to sort a given list in descending order without using the list method. 
def descending_order():
    array = [23,32,53, 76, 11, 21]
    print(f"The original array is {array}")
    for each in range(len(array)):
        for i in range(len(array) - each - 1):
            if array[i] < array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
         
    return array
result = descending_order()

print(f"The array in decending order is {result}")