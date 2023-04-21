# Write a Python program to remove spaces from a given string
def remove_space(name):
    string_with_out = ""

    for each in name:
        if each == " ":
            continue
        else:
            string_with_out += each
    return string_with_out
result = remove_space("This is Sabina.")   
print(result)

# for each in Name:
#     if each!= " ":
#         string_with_out += each

