# # Base class
# class Vehicle:
#     def __init__(self, speed):
#         self.speed = speed

#     def show_info(self):
#         print(f"Speed: {self.speed} km/h")


# # Subclass Car
# class Car(Vehicle):
#     def __init__(self, speed, fuel_type):
#         super().__init__(speed)
#         self.fuel_type = fuel_type

#     def show_info(self):
#         super().show_info()
#         print(f"Fuel Type: {self.fuel_type}")


# # Subclass Truck
# class Truck(Vehicle):
#     def __init__(self, speed, fuel_type):
#         super().__init__(speed)
#         self.fuel_type = fuel_type

#     def show_info(self):
#         super().show_info()
#         print(f"Fuel Type: {self.fuel_type}")


# # Subclass EVCar inheriting from Car
# class EVCar(Car):
#     def __init__(self, speed):
#         super().__init__(speed, fuel_type="Electric")

#     def charge_battery(self):
#         print("Battery is charging...")


# # 🔹 Test the classes

# print("== Car ==")
# car = Car(120, "Petrol")
# car.show_info()

# print("\n== Truck ==")
# truck = Truck(80, "Diesel")
# truck.show_info()

# print("\n== EV Car ==")
# ev = EVCar(150)
# ev.show_info()
# ev.charge_battery()
# Base class
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def show_info(self):
        print(f"Speed: {self.speed} km/h")


# Subclass Car
class Car(Vehicle):
    def __init__(self, speed, fuel_type):
        Vehicle.__init__(self, speed)  # manual call
        self.fuel_type = fuel_type

    def show_info(self):
        Vehicle.show_info(self)
        print(f"Fuel Type: {self.fuel_type}")


# Subclass Truck
class Truck(Vehicle):
    def __init__(self, speed, fuel_type):
        Vehicle.__init__(self, speed)
        self.fuel_type = fuel_type

    def show_info(self):
        Vehicle.show_info(self)
        print(f"Fuel Type: {self.fuel_type}")


# Subclass EVCar inheriting from Car
class EVCar(Car):
    def __init__(self, speed):
        Car.__init__(self, speed, fuel_type="Electric")  # manually calling Car constructor

    def charge_battery(self):
        print("Battery is charging...")


# 🔹 Test the classes

print("== Car ==")
car = Car(120, "Petrol")
car.show_info()

print("\n== Truck ==")
truck = Truck(80, "Diesel")
truck.show_info()

print("\n== EV Car ==")
ev = EVCar(150)
ev.show_info()
ev.charge_battery()
