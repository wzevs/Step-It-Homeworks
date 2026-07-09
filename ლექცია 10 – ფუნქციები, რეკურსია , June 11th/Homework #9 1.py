# Task N1
int_list = [10, 20, 30, 40]

def add_to_list(number):
    global int_list  
    int_list.append(number)

print("სია დამატებამდე:", int_list)
add_to_list(50)
print("სია დამატების შემდეგ:", int_list)



# Task N2
my_numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def get_sum_recursive(numbers_list):
    if not numbers_list:
        return 0
    return numbers_list[0] + get_sum_recursive(numbers_list[1:])

print(get_sum_recursive(my_numbers))



# Task N3
gl_str = "Global"

def local():
    gl_str = "Local"
    return gl_str  
_result = local()

print(f"ფუნქციის მიერ დაბრუნებული gl_str ს მნიშვნელობა: {_result}")
print(f"gl_str ს მნიშვნელობა ფუნქციის გარეთ: {gl_str}")



# Task N4
def sum_of_digits(number):
    if number < 10:
        return number
    last_digit = number % 10
    remaining_numbers = number // 10
    return last_digit + sum_of_digits(remaining_numbers)

result = sum_of_digits(12345)
print(f"ციფრების ჯამი არის: {result}")



# Task N5
def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]

print(reverse_string("Hello"))