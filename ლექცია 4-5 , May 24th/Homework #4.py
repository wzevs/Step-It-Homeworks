# Task N1
text = "გამარჯობა"
text_encoded = text.encode("utf-8")

print(f"ორიგინალი: {text}")
print(f"დაშიფრული: {text_encoded}")
print(f"მონაცემთა ტიპი: {type(text_encoded)}") 



# Task N2 (მოცემულობაში არ იყო დაკონკრეტებული თუ სიტყვა შეიცავს "python" სტრინგს, ვამატებთ თუ არა ბოლოში ისევ, ვიფიქრე რომ, ლოგიკურად თუ შეიცავს აღარ დავუმატო ბოლოში)
input_data = input("შეიყვანეთ ტექსტი :") 
cleaned_text = input_data.strip()
print(f"ტექსტი ზედმეტი ინტერვალების გარეშე: {cleaned_text}")
lowercase_text = cleaned_text.lower()
print(f"ტექსტი პატარა ასოებით : {lowercase_text}")
# ვამოწმებთ, არის თუ არა "python" ჩვენს პატარა ასოებიან ტექსტში
if "python" in lowercase_text:
    # თუ შეიცავს, უბრალოდ ჩავანაცვლებთ დიდი ასოთი და ბოლოში აღარაფერს ვამატებთ
    final_text = lowercase_text.replace("python", "Python")
else:
    # თუ არ შეიცავს, ბოლოში მივაწებებთ (მაგალითად, ინტერვალით და "Python"-ით)
    final_text = lowercase_text + " Python"
print(f"საბოლოო შედეგი : {final_text}")



# Task N3
text = input("შეიყვანეთ ტექსტი: ")
length = len(text)
half_index = length // 2
# თუ სიგრძე ლუწია
if length % 2 == 0:
    first_half = text[:half_index]
    print(f"ტექსტის სიგრძე ლუწია ({length}).")
    print(f"პირველი ნახევარი: '{first_half}'")
# თუ სიგრძე კენტია
else:
    first_half = text[:half_index]
    middle_char = text[half_index]  # ზუსტად შუა სიმბოლო
    print(f"ტექსტის სიგრძე კენტია ({length}).")
    print(f"პირველი ნახევარი შუა სიმბოლომდე: '{first_half}'")
    print(f"ცალკე გამოყოფილი შუა სიმბოლო: '{middle_char}'")



# Task N4
import string
text = input("შეიყვანეთ ტექსტი შესამოწმებლად: ")
has_letter = False
has_digit = False
is_valid = True
# თუ მომხმარებელმა არაფერი შეიყვანა 
if len(text) == 0:
    is_valid = False
else:
    for char in text:
        if char in string.ascii_letters:
            has_letter = True
        elif char in string.digits:
            has_digit = True
        else:
            # თუ სიმბოლო არც ასოა და არც ციფრი (მაგალითად: !, ~, #, $, ინტერვალი და ა.შ.)
            is_valid = False
            break

if is_valid and has_letter and has_digit:
    print("შედეგი: სტრიქონი ვალიდურია!")
else:
    print("შედეგი: სტრიქონი არავალიდურია!")



# Task N5
text = input("შეიყვანეთ ტექსტი: ")
print(f"\nორიგინალი ტექსტი: {text}")
print("-" * 40)

utf8_bytes = text.encode('utf-8')
utf8_decoded = utf8_bytes.decode('utf-8')
print("UTF-8")
print(f"ბაიტები: {utf8_bytes}")
print(f"ბაიტების რაოდენობა (ზომა): {len(utf8_bytes)} ბაიტი")
print(f"უკან დეკოდირებული: {utf8_decoded}")
print("-" * 40)

utf16_bytes = text.encode('utf-16')
utf16_decoded = utf16_bytes.decode('utf-16')
print("UTF-16")
print(f"ბაიტები: {utf16_bytes}")
print(f"ბაიტების რაოდენობა (ზომა): {len(utf16_bytes)} ბაიტი")
print(f"უკან დეკოდირებული: {utf16_decoded}")
print("-" * 40)

# ქართულ ტექსტზე ერორის ასარიდებლად უცნობი ასოები ჩავანაცვლოთ '?' ნიშნით
ascii_bytes = text.encode('ascii', errors='replace')
ascii_decoded = ascii_bytes.decode('ascii')
print("ASCII")
print(f"ბაიტები: {ascii_bytes}")
print(f"ბაიტების რაოდენობა (ზომა): {len(ascii_bytes)} ბაიტი")
print(f"უკან დეკოდირებული: {ascii_decoded}")
print("-" * 40)