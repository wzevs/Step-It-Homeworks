import os
import json

chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

filename = "chess_players.txt"

with open(filename, 'w', encoding='utf-8') as file:
    json.dump(chess_players, file, indent=4)

# Task N1
def get_file_path(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return os.path.abspath(file.name)

print("--- Task 1 ---")
print(get_file_path(filename))


# Task N2
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for player in data:
            print(player)

print("\n--- Task 2 ---")
read_file(filename)


# Task N3
def append_dict_to_json(filename, new_players_list):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for player in new_players_list:
        data.append(player)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

print("\n--- Task 3 ---")
new_players = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]
append_dict_to_json(filename, new_players)
read_file(filename)


# Task N4
def update_file_content(filename, completely_new_data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(completely_new_data, file, indent=4)

print("\n--- Task 4 ---")
fresh_data = [
    {'id': 777, 'name': 'Burduli', 'country': 'Georgia', 'rating': 2700, 'age': 30}
]
update_file_content(filename, fresh_data)
read_file(filename)