# Task N1
def print_fibonacci_recursive(n, seq=[0, 1]):
    if n <= 0:
        print("გთხოვთ შეიყვანოთ 0-ზე მეტი რიცხვი.")
        return
    if n == 1:
        print(0)
        return
    if len(seq) == n:
        print(*seq, sep=" ")
        return
    next_num = seq[-1] + seq[-2]
    print_fibonacci_recursive(n, seq + [next_num])

print_fibonacci_recursive(1000)



# Task N2
def is_anagram_recursive(str1, str2):
    def check(s1, s2):
        if len(s1) == 0 and len(s2) == 0:
            return True
        if len(s1) != len(s2):
            return False
        char = s1[0]
        if char not in s2:
            return False
        return check(s1[1:], s2.replace(char, "", 1))
    clean_str1 = str1.lower().replace(" ", "")
    clean_str2 = str2.lower().replace(" ", "")  
    return check(clean_str1, clean_str2)

print(is_anagram_recursive("race", "care"))        
print(is_anagram_recursive("Heart", "Earth"))      
print(is_anagram_recursive("hello", "world"))      



# Task N3
def factorial_recursive(n):
    if n < 0:
        return "შეცდომა"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(6))  



# Task N4
def count_character_recursive(text, char):
    if len(text) == 0:
        return 0
    if text[0] == char:
        return 1 + count_character_recursive(text[1:], char)
    else:
        return 0 + count_character_recursive(text[1:], char)

print(count_character_recursive("სალამი", "ა")) 
print(count_character_recursive("თბილისი", "ი")) 