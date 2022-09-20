from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, colour, wheels, age):
        self.colour = colour
        self.wheels = wheels
        self.age = age

    @abstractmethod  
    def fixVehicle(self):
        pass
   
class Car(Vehicle):
    def __init__(self, colour, wheels, age, doors, make):
        super().__init__(colour, wheels, age)
        self.doors = doors
        self.make = make
        
    def fixVehicle(self):

        baseCost = 150
        if self.age < 5:
            cost = baseCost * 1.1
        elif self.age >= 5 and self.age < 10:
            cost = baseCost * 1.7
        elif self.age >= 10:
            cost = baseCost * 2.0
            
        cost = baseCost + (self.wheels * 200) + (self.doors * 50)  

        return cost
            
            
class Motorbike(Vehicle):
    def __init__(self, colour, wheels, age, oil, battery):
        super().__init__(colour, wheels, age)
        self.oil = oil
        self.battery = battery
        
    def fixVehicle(self):

        baseCost = 250
        if self.age < 5:
            cost = baseCost * 1.1
        elif self.age >= 5 and self.age < 10:
            cost = baseCost * 1.6
        elif self.age >= 10:
            cost = baseCost * 1.9
            
        cost = baseCost + (self.wheels * 150)
        
        if self.battery == True:
            cost = cost + 100
        if self.oil == True:
            cost = cost + 75
            
        return cost
    
class Lorry(Vehicle):
    def __init__(self, colour, wheels, age, lightsToFix, brakes):
        super().__init__(colour, wheels, age)
        self.lightsToFix = lightsToFix
        self.brakes = brakes
        
    def fixVehicle(self):

        baseCost = 450
        if self.age < 5:
            cost = baseCost * 1.1
        elif self.age >= 5 and self.age < 10:
            cost = baseCost * 1.6
        elif self.age >= 10:
            cost = baseCost * 1.9
            
        cost = baseCost + (self.wheels * 300) + (self.lightsToFix * 70) + (self.brakes * 200)
        
        return cost  