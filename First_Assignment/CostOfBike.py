

cost = int(input("Enter the cost pruce of bike"))
if cost>10000:
    print(f"The road cost is {cost+(15/100)*cost}")
elif cost>50000 and cost<=100000:
    print(cost+(10/100)*cost)
elif cost<=50000:
    print(cost+(5/100)*cost)
