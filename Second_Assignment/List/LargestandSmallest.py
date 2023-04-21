# Write a program to find the largest and smallest element from a list
def largest_smallest():
    array = [2 , 35, 67, 37, 12]
    largest = array[0]

    for each in range(5):
        if array[each] > largest:
            largest = array[each]
    return largest
result = largest_smallest()
print(f"The largest number is {result}")
        
