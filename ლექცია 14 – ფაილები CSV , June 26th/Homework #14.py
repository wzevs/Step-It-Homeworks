import csv
import os

students = [
    {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
    {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
    {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
    {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
    {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
    {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
    {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
]

new_student = {
    'id': 5,
    'name': 'Demetre',
    'age': 18,
    'grade': 'A',
    'subject_name': 'Informatic',
    'mark': 94
}

filename = "students.csv"


# ---------------- CSV-ის შექმნა ----------------
def create_csv():
    # თუ ფაილი უკვე არსებობს, თავიდან აღარ გადავაწერთ (რომ არსებული მონაცემები არ დაიკარგოს)
    if os.path.exists(filename):
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "name", "age", "grade", "subject_name", "mark"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)
    except (IOError, OSError) as e:
        print(f"CSV ფაილის შექმნის შეცდომა: {e}")


# ---------------- მონაცემების წაკითხვა ----------------
def read_students():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა. ვქმნით ახალს...")
        create_csv()
        return []
    except (IOError, OSError) as e:
        print(f"ფაილის წაკითხვის შეცდომა: {e}")
        return []


# ---------------- მონაცემების ჩაწერა ----------------
def write_students(student_list):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "name", "age", "grade", "subject_name", "mark"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(student_list)
    except (IOError, OSError) as e:
        print(f"ფაილში ჩაწერის შეცდომა: {e}")


# ---------------- დამხმარე ფუნქცია: უნიკალური ID-ის შეყვანა ----------------
def get_unique_id(student_list, prompt="ID: "):
    existing_ids = {int(s["id"]) for s in student_list}

    while True:
        try:
            new_id = int(input(prompt))
        except ValueError:
            print("გთხოვთ შეიყვანოთ მთელი რიცხვი ID-სთვის.")
            continue

        if new_id in existing_ids:
            print(f"ID {new_id} უკვე დაკავებულია. გთხოვთ შეიყვანოთ სხვა ID.")
            continue

        return new_id


# ---------------- დამხმარე ფუნქცია: მთელი რიცხვის უსაფრთხო შეყვანა ----------------
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("გთხოვთ შეიყვანოთ სწორი მთელი რიცხვი.")


# ---------------- 1. სტუდენტის დამატება ----------------
def add_student():
    student_list = read_students()

    try:
        student_id = get_unique_id(student_list, "ID: ")
        name = input("Name: ")
        age = get_int_input("Age: ")
        grade = input("Grade: ")
        subject_name = input("Subject: ")
        mark = get_int_input("Mark: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "subject_name": subject_name,
            "mark": mark
        }

        student_list.append(student)
        student_list.sort(key=lambda x: int(x["id"]))

        write_students(student_list)
        print("სტუდენტი წარმატებით დაემატა.")
    except Exception as e:
        print(f"სტუდენტის დამატებისას მოხდა შეცდომა: {e}")


# ---------------- 2. ყველა ან ერთი სტუდენტის წაკითხვა ----------------
def show_students():
    student_list = read_students()

    if not student_list:
        print("სტუდენტების სია ცარიელია.")
        return

    student_id = input("Enter student id (Enter = all): ")

    if student_id == "":
        for student in student_list:
            print(student)
        return

    try:
        student_id = int(student_id)
    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი მთელი რიცხვი ID-სთვის.")
        return

    for student in student_list:
        try:
            if int(student["id"]) == student_id:
                print(student)
                return
        except (ValueError, KeyError):
            continue

    print("Student not found.")


# ---------------- 3. საშუალო ქულა საგნების მიხედვით ----------------
def average_marks():
    student_list = read_students()

    if not student_list:
        print("სტუდენტების სია ცარიელია.")
        return

    subjects = {}

    for student in student_list:
        try:
            subject = student["subject_name"]
            mark = int(student["mark"])
        except (ValueError, KeyError) as e:
            print(f"არასწორი მონაცემი გამოტოვებულია: {e}")
            continue

        if subject not in subjects:
            subjects[subject] = []

        subjects[subject].append(mark)

    if not subjects:
        print("საშუალო ქულის გამოსათვლელად მონაცემი არ მოიძებნა.")
        return

    for subject, marks in subjects.items():
        print(subject, sum(marks) / len(marks))


# ---------------- 4. ქულის განახლება ----------------
def update_mark():
    student_list = read_students()

    if not student_list:
        print("სტუდენტების სია ცარიელია.")
        return

    try:
        student_id = get_int_input("Student ID: ")
        subject = input("Subject: ")
        new_mark = get_int_input("New mark: ")
    except Exception as e:
        print(f"შეყვანისას მოხდა შეცდომა: {e}")
        return

    found = False
    for student in student_list:
        try:
            if int(student["id"]) == student_id and student["subject_name"] == subject:
                student["mark"] = new_mark
                found = True
        except (ValueError, KeyError):
            continue

    if found:
        write_students(student_list)
        print("ქულა წარმატებით განახლდა.")
    else:
        print("სტუდენტი მითითებული საგნით ვერ მოიძებნა.")


# ---------------- 5. მოცემული სტუდენტის დამატება ----------------
def add_given_student():
    student_list = read_students()

    try:
        existing_ids = {int(s["id"]) for s in student_list}

        if int(new_student["id"]) in existing_ids:
            print(f"ID {new_student['id']} უკვე დაკავებულია, სტუდენტი ვერ დაემატა.")
            return

        student_list.append(new_student)
        student_list.sort(key=lambda x: int(x["id"]))

        write_students(student_list)
        print("სტუდენტი წარმატებით დაემატა.")
    except Exception as e:
        print(f"სტუდენტის დამატებისას მოხდა შეცდომა: {e}")


def main():
    create_csv()

    while True:
        print("\n------ MENU ------")
        print("1. Add student")
        print("2. Show students")
        print("3. Average marks")
        print("4. Update mark")
        print("5. Add given student")
        print("0. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                add_student()

            elif choice == "2":
                show_students()

            elif choice == "3":
                average_marks()

            elif choice == "4":
                update_mark()

            elif choice == "5":
                add_given_student()

            elif choice == "0":
                print("Program finished.")
                break

            else:
                print("Invalid choice.")

        except KeyboardInterrupt:
            print("\nპროგრამა შეწყდა მომხმარებლის მიერ.")
            break
        except Exception as e:
            print(f"მოულოდნელი შეცდომა: {e}")

#იდეაში აქ არ გვჭირდება, მაგრამ ამის გააზრებით კლასებზე უფრო მეტი გავიგე
if __name__ == "__main__":
    main()