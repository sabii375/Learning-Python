#7. Write a program to find the common items in two lists.
def common_items():
    list1 = ["apple", "praman", "cow"]
    list2 = ["beepla", "praman", "apple"]
    common = []
    for each in range(len(list1)):
        for eachh in range(len(list2)):
            if list1[each] == list2[eachh]:
                common.append(list2[eachh])
    return common
result = common_items()
print(f"The common items are {result}")
