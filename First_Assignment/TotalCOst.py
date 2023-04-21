#If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred. 

price = int(input("Enter the price of the item:"))
sell_price= int(input("Enter the selling price of the item:"))
if price>sell_price:
    price2=price-sell_price
    print(f"The selleer made the loss by {price2}")
else:
    price3= sell_price-price
    print(f"The selleer made the profit by {price3}") 