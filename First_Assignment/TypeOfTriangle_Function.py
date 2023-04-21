def triangle(a,b,c):
    if a==b and a==c:
        print("The triangle is equilateral.")
    elif a!=b and a!=c:
        print("The trinagfle is scalene.")
    else:
        print("The trianlge is isosceles.") 
a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))
triangle(a,b,c)