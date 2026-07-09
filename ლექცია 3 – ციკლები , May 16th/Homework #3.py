# Task N1
n = int(input("შეიყვანეთ რიცხვი :"))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"1-დან {n}-მდე რიცხვების ჯამი არის: {total_sum}")


# Task N2
x = int(input("შეიყვანეთ რიცხვი :"))
while x != 0:
    print(x)
    x -= 1

# Task N3
y = 7
while y != x:
    x = int(input("შეიყვანეთ რიცხვი :"))
print(f"თქვენ გამოიცანით! ჩაფიქრებული რიცხვია {y}")

# Task N4
total_sum = 0
while True:
    user_input = input("შეიყვანეთ რიცხვი ან 'sum' დასასრულებლად: ")
    if user_input == "sum":
        break
    n = int(user_input)
    if n > 0:
        total_sum = total_sum + n
print("დადებითი რიცხვების ჯამი არის:", total_sum)