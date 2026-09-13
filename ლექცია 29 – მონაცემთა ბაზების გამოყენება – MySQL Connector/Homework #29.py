import mysql.connector

# მონაცემთა ბაზასთან დაკავშირება
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwerty123!", 
    database="lesson27_hw" 
)

cursor = db.cursor()

# ძველი ცხრილის წაშლა, რათა კოდის მრავალჯერ გაშვებისას დუბლიკატები არ შეიქმნას
cursor.execute("DROP TABLE IF EXISTS student")

# სტუდენტის ცხრილის შექმნა
cursor.execute("""
    CREATE TABLE student (
        studentID INT AUTO_INCREMENT PRIMARY KEY,
        studentFirstName VARCHAR(50),
        studentLastName VARCHAR(50),
        studentAge INT
    )
""")

# საწყისი 5 მონაცემის შეტანა
insert_query = "INSERT INTO student (studentFirstName, studentLastName, studentAge) VALUES (%s, %s, %s)"
initial_data = [
    ('გრიგოლ', 'აბულაძე', 31),
    ('ანა', 'გერგაული', 25),
    ('ქეთევან', 'კახიძე', 26),
    ('ანდრო', 'შალიკაშვილი', 29),
    ('ნინო', 'ხარაზიშვილი', 24)
]

cursor.executemany(insert_query, initial_data)
db.commit()

# საწყისი მონაცემების დაბეჭდვა
print("საწყისი 5 მონაცემი:")
cursor.execute("SELECT studentLastName, studentFirstName, studentAge FROM student")
for row in cursor.fetchall():
    # {:<15} გამოიყენება ტექსტის გასასწორებლად, რომ სვეტები ერთმანეთს დაემთხვეს
    print(f"{row[0]:<15} {row[1]:<15} {row[2]}")

print("\n----------------------------------------------\n")

# კიდევ ერთი მონაცემის ჩამატება (კახიძე კოტე)
new_student = ('კოტე', 'კახიძე', 27)
cursor.execute(insert_query, new_student)
db.commit()

# საბოლოო შედეგის დაბეჭდვა, დალაგებული ანბანის მიხედვით (გვარი, შემდეგ სახელი)
print("საბოლოო სახე:")
cursor.execute("""
    SELECT studentLastName, studentFirstName, studentAge 
    FROM student 
    ORDER BY studentLastName ASC, studentFirstName ASC
""")

for row in cursor.fetchall():
    print(f"{row[0]:<15} {row[1]:<15} {row[2]}")

# კავშირის დახურვა
cursor.close()
db.close()