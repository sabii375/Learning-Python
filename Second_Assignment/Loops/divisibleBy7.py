# Write a program to find the number of and sum of all integers greater than 100 and less than 200 that are divisible by 7.
def divisible_by_seven():
    sum = 0
    count = 0
    for i in range(100,201):
        if i % 7 == 0:
            sum = sum + i
            count = count + 1
    return sum, count
sum,count = divisible_by_seven()
print(f"The number and sum of integer that is divisible by seven are {count} and {sum}")