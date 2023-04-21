#Write a program to find the mean value of a given a list. 
def mean_value():
    array = [2,3,1,4]
    summ = 0
    for each in range(len(array)):
        summ += array[each] 
    mean = summ/len(array)
    return mean
result = mean_value()
print(f"The mean value of the given list is {result}")
