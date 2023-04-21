 
def largest_smallest(a,b,c):
    if a>=b and a>=c:
        largest=a
    elif b>=a and b>=c:
        largest=b
    else:
        largest=c
    
    if a<=b and a<=c:
        smallest=a
    elif b<=a and b<=c:
        smallest=b
    else:
        smallest=c

    return largest,smallest

largest,smallest = largest_smallest(85,45,20)
print(f"The largest age is {largest} and the smallest age is {smallest}")   