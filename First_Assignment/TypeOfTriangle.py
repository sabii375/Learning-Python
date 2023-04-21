a= int(input("Enter the frist side of triangle:"))
b= int(input("Enter the second side of triangle:"))
c= int(input("Enter the third side of triangle:"))
if a==b and a==c:
    print("The triangle is equilateral.")
elif a!=b and a!=c:
    print("The trinagfle is scalene.")
else:
    print("The trianlge is isosceles.")    

    