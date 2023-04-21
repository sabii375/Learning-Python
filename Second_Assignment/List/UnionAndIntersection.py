# Write a program to find the union and intersection of two lists. 

def intersection():
    list1 = [ 12,21,3,4,5,5]
    list2 = [ 23, 5,7,9,89]
    intersection = []
    union = []

    for i in list1:
        for j in list2:
            if i == j:
                intersection.append(i)
    return intersection
print(intersection())

def union():
    list1 = [ 12,21,3,4,5]
    list2 = [ 23, 5,7,9,89]
    for each in list2:
        if each not in list1:
            list1.append(each)
        
    # result = list1 + list2
    # print(f"Length of result {len(result)}")

    # for i in range(len(result)):
    #     print(f"i={i}")
    #     for j in range(len(result)):
    #         print(f"j={j}")
    #         if i == j:
    #             continue
    #         if result[i] == result[j]:
    #             x = result.pop(j)
    #     print("\n")        
    return list1
print(union())
