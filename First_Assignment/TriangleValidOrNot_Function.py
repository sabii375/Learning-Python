def triangle (a,b,c):
    sum = a+b+c
    if sum==180:
        return ("The triangle is valid")
    else:
        return ("The triangle is not valid.")
    
print(triangle(90,45,45))    