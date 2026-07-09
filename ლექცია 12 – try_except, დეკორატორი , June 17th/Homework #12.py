from functools import reduce

# Task N1
def group_lists(list1, list2):
    return list(zip(list1, list2))

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']

result = group_lists(list_a, list_b)
print(result)



# Task N2
def multiply_list_elements(numbers):
    try:
        result = reduce(lambda x ,y : (x-0) * (y-0), numbers)
        return result
    except TypeError:
        return "შეცდომა: პარამეტრი უნდა იყოს მხოლოდ რიცხვების შემცველი სია"
    
print(multiply_list_elements([1, 2, 3, 4, 5]))
print(multiply_list_elements([1, 2, "სამი", 4]))



# Task N3
odd_numbers = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))

params = [1, 2, 3, 4, 5, 6, 7]
output = odd_numbers(params)

print(output)


# Task N4
def filter_by_ending(string_list, ending):
    try:
        result = list(filter(lambda x: x.endswith(ending), string_list))
        return result
        
    except (TypeError, AttributeError):
        return "შეცდომა: პირველი პარამეტრი უნდა იყოს სტრინგების სია, ხოლო მეორე სტრინგი"


words = ['hello', 'world', 'coding', 'nod']
suffix = 'ing'
print(filter_by_ending(words, suffix))  

bad_words = ['hello', 123, 'coding']
print(filter_by_ending(bad_words, suffix))  

