
class Vehicle:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def display_details(self):
        print(f"Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}")


class Car(Vehicle):
    def display_car(self):
        print("Car class object.")
        print(f"Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}\n")
        # self.display_details()

class Truck(Vehicle):
    def display_truck(self):
        print("Truck class object.")
        print(f"Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}\n")

class ElectricVehicle(Vehicle):
    def __init__(self, model, color, year, battery, range):
        super().__init__(model, color, year)
        self.battery = battery
        self.range = range

    def display_electric_vehicle(self):
        print("Electric vehicle class object.")
        # print(f"Model: {self.model}, \nColor: {self.color}, \nYear: {self.year}\nBattery capacity: {self.battery}mAh\nRange: {self.range}Km")
        self.display_details()
        print(f"Battery capacity: {self.battery}mAh\nRange: {self.range}Km")



car = Car("polo", "navy blue", 2022)
# car.display_details()
car.display_car()

truck = Truck("Scania", "White", 2024)
truck.display_truck()
# truck.display_details()

# electric = ElectricVehicle(model="KIA", color="Black", year=2023, battery=25000, range=300)
electric = ElectricVehicle("KIA", "Black", 2023, 25000, 300)
electric.display_electric_vehicle()

