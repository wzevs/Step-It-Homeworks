#Task N1
input_data = input("შეიყვანეთ ელემენტები გამოყოფილი მძიმით: ")
elements = [item.strip() for item in input_data.split(',')]
unique_data = set(elements)
print("უნიკალური მონაცემების სიმრავლე (set):")
print(unique_data)



#Task N2
input_data = input("შეიყვანეთ ელემენტები გამოყოფილი მძიმით: ")
elements = [item.strip() for item in input_data.split(',')]
unique_immutable_data = frozenset(elements)
print("უნიკალური, შეუცვლელი სიმრავლე (frozenset):")
print(unique_immutable_data)


#Task N3
set1 = {"Python", "Java", "C++"}
set2 = {"JavaScript", "Python", "Go"}
union_set = set1.union(set2)
result_tuple = tuple(union_set)
print("პირველი set:", set1)
print("მეორე set:", set2)
print("გაერთიანებული კორტეჟი (tuple):", result_tuple)



#Task N4
input_data = input("შეიყვანეთ რიცხვები მძიმით გამოყოფილი: ")
num_tuple = tuple(int(x.strip()) for x in input_data.split(','))
unique_list = list(set(num_tuple))
print("საწყისი კორტეჟი (tuple):", num_tuple)
print("უნიკალური ელემენტების სია (list):", unique_list)



#Task N5
students = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
for name, age in students:
    print(f"Name: {name}, Age: {age}")


#Task N6
list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
common_users = set(list1).intersection(set(list2))
print("თანხვედრა (საერთო მომხმარებლები):", list(common_users))