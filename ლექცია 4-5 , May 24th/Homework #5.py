# Task N1
my_list = []
print("პროგრამა დაიწყო!")
print("ბრძანებები: a (დამატება), r (წაშლა), e (გამოსვლა)")

while True:
    print(f"\nმიმდინარე სია: {my_list}")
    command = input("შეიყვანეთ ბრძანება (a/r/e): ")
    
    # დამატების ლოგიკა 
    if command == 'a':
        # ვიღებთ რიცხვს და გადაგვყავს მთელ რიცხვში
        number = int(input("რა რიცხვის დამატება გსურთ? "))
        my_list.append(number)
        print(f"{number} დაემატა სიაში.")
        
    # წაშლის ლოგიკა 
    elif command == 'r':
        number = int(input("რა რიცხვის წაშლა გსურთ? "))
        
        # ჯერ ვამოწმებთ, ნამდვილად არის თუ არა ეს რიცხვი სიაში
        if number in my_list:
            my_list.remove(number)
            print(f"{number} წაიშალა სიიდან.")
        else:
            print("შეცდომა: ასეთი რიცხვი სიაში არ მოიძებნა!")
            
    # გამოსვლის ლოგიკა
    elif command == 'e':
        print("\nპროგრამამ დაასრულა მუშაობა.")
        print(f"საბოლოო შედეგი: {my_list}")
        break  # შევწყვიტოთ while ციკლი
        
    else:
        print("არასწორი ბრძანება! გთხოვთ შეიყვანოთ მხოლოდ 'a', 'r' ან 'e'.")



# Task N2
my_list_1 = [43, '22', 12, 66, 210, ["hi"]]
print(f"საწყისი სია: {my_list_1}\n")

# დავბეჭდოთ 210-ის ინდექსი
index_of_210 = my_list_1.index(210)
print(f"210-ის ინდექსია: {index_of_210}")

# დავამატოთ ბოლო ელემენტში ტექსტი "hello"
my_list_1[-1].append("hello")
print(f"სიის მდგომარეობა 'hello'-ს დამატების შემდეგ: {my_list_1}")

# წავშალოთ მე-2 ინდექსზე მდგომი ელემენტი და დავბეჭდოთ
my_list_1.pop(2)  # ასევე შეიძლებოდა: del my_list_1[2]
print(f"მე-2 ინდექსის წაშლის შემდეგ: {my_list_1}\n")

# შევქმნათ ახალი სია my_list_2, გავასუფთავოთ და დავბეჭდოთ ორივე
my_list_2 = my_list_1.copy()
my_list_2.clear()

print("საბოლოო შედეგები:")
print(f"my_list_1 (ორიგინალი): {my_list_1}")
print(f"my_list_2 (გასუფთავებული): {my_list_2}")



# Task N3
import re
phone_number = input("შეიყვანეთ ტელეფონის ნომერი: ")

# ვადგენთ Regex შაბლონს "(123) 456-789" ფორმატისთვის
pattern = r"\(\d\d\d\) \d\d\d-\d\d\d"

if re.fullmatch(pattern, phone_number):
    print(f"შედეგი: {phone_number}")
else:
    print("Invalid format")