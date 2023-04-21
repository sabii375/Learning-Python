#1 Write a python program to ask for a number from user. Then display if the number is odd or even. 
num=int(input("Enter any number:"))
if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")    



#2 Write a program to check if an input number is divisible by 7 or not.
num1 = int(input("Enter the number:"))
if num1%7==0:
    print("The number is divisible by seven.")
else:
    print("The number is not divisible by seven.")   



#3 Write a program to display the last digit of a number.      
num1 = int(input("Enter any number:"))
num2 = num1%10
print(f"The last digit of the number is {num2}")



#4 Write a program to read the age of three people from the user and display the smallest and biggest among them. 
num1=int(input("Enter the age of first person:"))
num2=int(input("Enter the age of second person:"))
num3=int(input("Enter the age of third person:"))
if num1>=num2 and num1>=num3:
    print("Person 1 has the oldest age.")
elif num2>=num1 and num2>=num3:
    print("Person 2 has the oldest age.")
else:
    print("Person 3 has the oldest age.")

if num1<=num2 and num1<=num3:
    print("Person 1 has the smallest age.")
elif num2<=num1 and num2<=num1:
    print("Person 2 has the smallest age.")    
else:
    print("Person 3 has the smallest age.")


    
# 5 While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If quantity and price per item are input through the keyboard, write  a program to calculate the total expenses
item = int(input("Enter the quantity of the item:"))
price = int(input("Enter the price of the item:"))
if item>1000:
    price_discounted = price-(10*price)/100
    print(f"The total cost is {price_discounted}")
else:
    print(f"The total cost is {price}")    


#6 Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
a= int(input("Enter the first angle:"))
b= int(input("Enter the second angle:"))
c= int(input("Enter the third angle:"))
total = a+b+c
if total==180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")