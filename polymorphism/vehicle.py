from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    car_increased_consumption = 0.9

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Car.car_increased_consumption)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    truck_increased_consumption = 1.6
    truck_fuel_loss = 0.95

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Truck.truck_increased_consumption)
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.truck_fuel_loss