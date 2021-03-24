# Exercises
#
# # Task 1: year_of_birth function
#
# def year_of_birth(age, name, bday):
#     current_year = 2021
#     if bday == "y":
#         birth_year = current_year - age
#     else:
#         birth_year = current_year - (age + 1)
#     return f"OMG {name}, you are {age} years old so you were born in {birth_year}"
#
#
# name = input("What is your name? ")
# age = int(input("What is your age? "))
# birthday = input("Have you already had your birthday this year? Y/N ")
# print(year_of_birth(age, name, birthday))
#
#
# # Task 2: Restaurant waiter helper
# menu = ["chicken", "lamb", "beef"]
# print("Items on the menu are:")
# for item in menu:
#     print(item)
# order_list = []
# for i in range(3):
#     order = input("What would you like to order? ")
#     if order in menu:
#         order_list.append(order)
#     else:
#         print("Your order is not available, please pick something else.")
#         for item in menu:
#             print(item)
# print("Your order is: ")
# for item in order_list:
#     print(item)
#
# # Task 3: xmas gifts
# xmas_gifts = []
# item = input("What would you like to add to Xmas gifts list? ")
# while "exit" not in item:
#     xmas_gifts.append(item)
#     item = input("What would you like to add to Xmas gifts list? ")
# for item in xmas_gifts:
#     print(f"# {xmas_gifts.index(item) +1} - {item}")

# # Task 4: Fizz Buzz
# for i in range(1, 100, 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)


# Task 5: Functional Calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def area_circle(radius):
    return 3.14 * (radius ** 2)

def area_square(side):
    return side ** 2

def area_triangle(base, height):
    return 0.5 * base * height

# print(add(4, 5))
# print(subtract(4, 5))
# print(multiply(4, 5))
# print(divide(4, 5))
#
# print(area_circle(3))
# print(area_square(4))
# print(area_triangle(2, 3))

# Task 6: Loops and lists
for i in range(10):
    print("Hello!")

list_names = []
for i in range(5):
    names = input("What is your name? ")
    list_names.append(names)

list_names_lower = []
for item in list_names:
    list_names_lower.append(item.lower())

for name in list_names_lower:
    if len(name) % 2 == 0:
        print(f"{name} is even")
    else:
        print(f"{name} is not even")
