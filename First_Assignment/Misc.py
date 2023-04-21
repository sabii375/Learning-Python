

# print("sabina Thapa")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/   |")

# print("There once was a man named Beepla,")
# print("he is 34 yeras old.")
# print("He really liekd the name Beepla,")
# print("But didnot like being 34.")

# term = "Sabina Thapa"
# # print(term + " is talent")
# # print(term.upper().islower())

# print(term.replace("Sabina", "Beeplaw"))


# print((3*4)+5)
# print(pow(3,2))

# num = 4
# print(str(num)+ " is my favourite number")
# print(round(4.8))

# from math import *

# print(sqrt(2))

# name = input("Enter your name: ")
# age = input("Enter your age:")
# print("Hello "+ name + " Your age is " + age)

# num1 = input("Enter the firts number: ")
# num2 = input("Enter the second number: ")
# sum = float(num1) + float(num2)
# print("The sum is " + str(sum))

# list
# frinds = ["Beepla", "Sam", "Prasuma", "sazina", , "Ram"]
# frinds[1]= "Sabi"
# print(frinds[1:4])

# lists function
# lucky_numbers=[3,3,2,1,4,56]
# friends = ["BEEPLA", "SABIU", "MAGU"]
# friends.sort()
# print(friends )

#beepla questionb
# arr=[]
# l1=input("Enter the first element of list:")
# l2=input("Enter the second element of list:")
# l3=input("Enter the third element of list:")
# arr.append(l1)
# arr.append(l2)
# arr.append(l3)
# print(arr)
# arr.pop()
# print(arr)



# #question 2
# num1=float(input("Enter the float number"))
# s=num1*100
# print(f"The number is {s}")

#Tuples
# coordinates=(4,5)

# print(coordinates[0])

#function
# def say_hi(name, age):
#     print(f"Hi {name}. You are {age}")

# say_hi("Sabina",21)

#return
# def square(num):
#    return num*num

# result = square(2)

# print(result)


#if statements using boolean
# is_male = False
# is_tall = True
# if is_male and is_tall:
#     print("You are a male or tall or both ")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not male but tall")    
# else:
#     print("You are not male and not tall ")


#if statement and comparison
# def max_num(num1, num2,num3):
#     if num1>=num2 and num1>=num3:
#         return num1
#     elif num2>=num1 and num2>=num3:
#         return num2
#     else:
#         return num3
# print(max_num(3,4,5))

#Advance calculator
# num1=float(input("Enter the frist number."))
# op=input("Enter the operator.")
# num2=float(input("Enter the second number"))

# if op =="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("Invalid operator.")

#Dictionay
# monthConversion = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "Novemver",
#     "Dec": "December",
# }

# print(monthConversion["Nov"])
# print(monthConversion.get("Dec"))



#While loop
# i=1
# while i <= 10:
#     print(i)
#     i += 1 #(i=i+1)

# print("Done with loop")


#Build a basic guessing game
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess!= secret_word:
#     guess = input("Enter guess:")
#     guess_count += 1

# print("Succesfull guess.")


#For loop
# for letter in "Giraffe Academy":
#     print(letter)

# friends=["SABI","BEEP","HII"]
# for name in friends:
#     print(name)

# for index in range(len(friends)):
#     print(friends[index])

# for index in range(5):
#     if index == 0:
#         print("First iteration.")
#     else:
#         print("Not first")




#Exponenet Function
# def raise_to_power(base_num,pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
# print(raise_to_power(2,3))



#2D list
# number_grid = [ 
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# for row in number_grid:
#     for column in row:
#         print(column)


#Build a translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation= translation+"g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase")))


#catching errors
# try:

#     number=int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid input")

#Reading files
# employee_file = open("employee.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)

# print(employee_file.read())
# employee_file.close()

#writing files
# employee_file = open("employee1.txt","w")
# employee_file.write("Tobby = Human resources")
# employee_file.close()


# httml = open("index.html","w")
# httml.write("<p>This is a paragraph</p>")
# httml.close()


#Using modules and pips
# import useful_tools
# print(useful_tools.roll_dice(10))
