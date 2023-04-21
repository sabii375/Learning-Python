#Write a program to convert a list of multiple integers into a single integer. Example: [11,33,50] into 113350.

def single_integer():
    letter = [ 23, 34, 45 ]
    single = ''
    for each in letter:
        single += str(each)
    return single
result = single_integer()
print(result)