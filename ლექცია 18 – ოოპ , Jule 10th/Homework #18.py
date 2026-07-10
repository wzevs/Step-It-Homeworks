from datetime import datetime

# Task N1

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __str__(self):
        return f"({self.x},{self.y})"

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v1)
print(v2)
print(v3)



# Task N2

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2)
print(book1 == book3)



# Task N3

class Car:

    def __new__(cls, *args, **kwargs):
        print(f"__new__ გამოძახებულია {cls.__name__} კლასისთვის — იქმნება ობიექტი")
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        print("__init__ გამოძახებულია — ხდება ატრიბუტების ინიციალიზაცია")
        # ვიყენებთ setter-ებს (property.setter), რათა ვალიდაცია
        # ინიციალიზაციისასაც მუშაობდეს
        self.brand = brand
        self.model = model
        self.year = year

    # ---------- brand ----------
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("brand უნდა იყოს არაცარიელი სტრიქონი")
        self._brand = value.strip()

    # ---------- model ----------
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("model უნდა იყოს არაცარიელი სტრიქონი")
        self._model = value.strip()

    # ---------- year ----------
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError("year უნდა იყოს მთელი რიცხვი (int)")
        current_year = datetime.now().year
        if value < 1886 or value > current_year:
            raise ValueError(
                f"year უნდა იყოს 1886-სა და {current_year}-ს შორის"
            )
        self._year = value

    def car_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")


if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020)
    car1.car_info()

    # get/set-ის შემოწმება
    car1.brand = "Honda"
    car1.model = "Civic"
    car1.year = 2021
    car1.car_info()

    # ვალიდაციის შემოწმება — გამოიწვევს შეცდომას
    try:
        car1.year = "ორი ათასი ოცდაერთი"
    except ValueError as e:
        print(f"შეცდომა: {e}")

    try:
        car1.year = 1500
    except ValueError as e:
        print(f"შეცდომა: {e}")

    try:
        car1.brand = ""
    except ValueError as e:
        print(f"შეცდომა: {e}")