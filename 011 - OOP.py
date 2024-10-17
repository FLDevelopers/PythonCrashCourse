# Basic Class
class Car:
    def __init__(self, make, model, year):
        # The __init__ method is the constructor of the class. It is called when a new object is created.
        # Attributes are defined here and attached to the object.
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # This method prints the details of the car.
        print(f"Car: {self.year} {self.make} {self.model}")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()


#Encapsulation
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def display_info(self):
        print(f"Car: {self.__year} {self.__make} {self.__model}")

    # Method to update the year
    def update_year(self, new_year):
        self.__year = new_year

# Creating an object
my_car = Car("Honda", "Civic", 2018)
my_car.display_info()

# Trying to update the year via method
my_car.update_year(2022)
my_car.display_info()


# Inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle: {self.year} {self.make} {self.model}")

# Derived class
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)  # Call the parent class's constructor
        self.battery_capacity = battery_capacity  # New attribute specific to ElectricVehicle

    def display_info(self):
        super().display_info()  # Call the parent class's display_info method
        print(f"Battery capacity: {self.battery_capacity} kWh")

# Creating an object of the ElectricVehicle class
my_electric_vehicle = ElectricVehicle("Tesla", "Model X", 2023, 120)
my_electric_vehicle.display_info()



# Polymorphism
class NewCar:
    def drive(self):
        print("The car is driving using gasoline.")

class ElectricCar(NewCar):
    def drive(self):
        print("The electric car is driving using electricity.")

# Creating objects of both classes
my_car = NewCar()
my_electric_car = ElectricCar()

# Demonstrating polymorphism
for car in (my_car, my_electric_car):
    car.drive()


# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("The car starts with a key.")

class ElectricCar(Vehicle):
    def start(self):
        print("The electric car starts with a button.")

# Objects of subclasses
my_car = Car()
my_electric_car = ElectricCar()

my_car.start()
my_electric_car.start()
