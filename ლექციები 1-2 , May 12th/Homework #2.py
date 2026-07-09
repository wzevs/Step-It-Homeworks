# Task N1
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

user_number = int(input("Enter a number: "))

if user_number in num_list:
    print("The number in list")
else:
    print("The number not in list")

# Task N2
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Task N3
str1 = "Hello"
str2 = "Hello"

if str1 is str2:
    print("Same object")
else:
    print("Different object")

# Task N4
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

user_number = int(input("Enter a number: "))

if user_number > num_list[2] and user_number < num_list[-1]:
    print("More than list elements")
elif user_number == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")