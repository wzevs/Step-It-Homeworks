from datetime import datetime

class Car:

    number_of_cars = 0  # კლასის ატრიბუტი

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.number_of_cars += 1  # ყოველ შექმნაზე იზრდება

    @classmethod
    def total_cars(cls):
        print(f"მანქანების მთლიანი რაოდენობა: {cls.number_of_cars}")

    def age_of_car(self):
        current_year = datetime.now().year
        return current_year - self.year

    def car_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Age: {self.age_of_car()} years")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"{self.brand} {self.model}_ის ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს")


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("BMW", "X5", 2022)
electric_car1 = ElectricCar("Tesla", "Model 3", 2023, 500)
electric_car2 = ElectricCar("Nissan", "Leaf", 2021, 400)
car1.car_info()
car2.car_info()
electric_car1.car_info()
electric_car1.battery_info()

print(f"სულ შექმნილი მანქანების რაოდენობა: {Car.number_of_cars}")

Car.total_cars()