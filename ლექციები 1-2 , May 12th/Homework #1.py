# Task N1
first_number = int(input("შეიყვანეთ პირველი რიცხვი A: "))
second_number = int(input("შეიყვანეთ მეორე რიცხვი B: "))

print("A + B =", first_number + second_number)
print("A - B =", first_number - second_number)
print("B - A =", second_number - first_number)
print("A * B =", first_number * second_number)
print("A / B =", first_number / second_number)
print("B / A =", second_number / first_number)
print("A // B =", first_number // second_number)
print("B // A =", second_number // first_number)
print("A % B =", first_number % second_number)
print("B % A =", second_number % first_number)
print("A ** B =", first_number ** second_number)
print("B ** A =", second_number ** first_number)

# Task N2
first_number = int(input("შეიყვანეთ დიაგონალის სიგრძე A: "))
second_number = int(input("შეიყვანეთ დიაგონალის სიგრძე B: "))

print("რომბის ფართობი ტოლია: ", (first_number * second_number) / 2)


# Task N3
number = int(input("შეიყვანეთ რიცხვი მეტრებში: "))

print("შეყვანილი რიცხვი სანტიმეტრებში გახლავთ :", number * 100)
print("შეყვანილი რიცხვი დეციმეტრებში გახლავთ :", number * 10)
print("შეყვანილი რიცხვი მილიმეტრებში გახლავთ :", number * 1000)
print("შეყვანილი რიცხვი მილებში გახლავთ :", number / (1609.34))

# Task N4
first_number = int(input("შეიყვანეთ სიმაღლე : "))
second_number = int(input("შეიყვანეთ ფუძე : "))

print("სამკუთხედის ფართობი ტოლია: ", (first_number * second_number) / 2)

# Task N5
number = int(input("შეიყვანეთ ორნიშნა რიცხვი: "))

first_digit = number // 10
second_digit = number % 10
print("შეყვანილი რიცხვის, ციფრების ჯამია :", first_digit + second_digit)