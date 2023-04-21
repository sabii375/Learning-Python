def cost(price,sell_price):
    if price>sell_price:
        loss=price-sell_price
        print("The total loss is"+loss)
    else:
        profit= sell_price-price
        print(f"The total profit is {profit}")
cost(5000,5500)    
 