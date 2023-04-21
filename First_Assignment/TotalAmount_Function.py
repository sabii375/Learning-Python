def total_cost(quantity,item):
    if quantity>1000:
        price_discounted = item-(10*item)/100
        return price_discounted
    else:
        return item
    
total = total_cost(5000,500)
print(f"The total cost is {total}")
