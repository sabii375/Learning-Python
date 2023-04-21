# Write a Python function to create an HTML string with tags around the word(s). 
def html_code(tag, element):
    print(f"<{tag}>{element}</{tag}>")
tag = input("Enter the tag: ")
element = input("Enter the element: ")
html_code(tag,element)