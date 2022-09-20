from vehicles import *

current_vehicles = []
bill_repair = []

def add_car():
    print("Enter car details")
    customer_name = input("Enter Customer Name: ")
    vehicle_type = "Car"
    new_car = Car(input("Colour of car = "), int(input("Number of wheels = ")), int(input("Age of car = ")), int(input("Number of doors = ")), input("Make of car = "))
    carName = ("customer name: "+customer_name), " " + ("Vehicle type = "+vehicle_type)
    current_vehicles.append(carName)
    cost_of_repair = new_car.fixVehicle()
    bill_repair.append(cost_of_repair)
    

def add_motorbike():
    print("Enter motorbike details")
    customer_name = input("Enter Customer Name: ")
    vehicle_type = "Motorbike"
    new_bike = Motorbike(input("Colour of bike = "), int(input("Number of wheels = ")), int(input("Age of bike = ")), input("Oil change(True/False) = "), input("New battery(True/False) = "))
    bikeName = ("customer name: "+customer_name), " " + ("Vehicle type = "+vehicle_type)
    current_vehicles.append(bikeName)
    cost_of_repair = new_bike.fixVehicle()
    bill_repair.append(cost_of_repair)

    
def add_lorry():
    print("Enter lorry details")
    customer_name = input("Enter Customer Name: ")
    vehicle_type = "Lorry"
    new_lorry = Lorry(input("Colour of lorry = "), int(input("Number of wheels = ")), int(input("Age of lorry = ")), int(input("Number of lights to fix = ")), int(input("Number of brakes to fix = ")))
    lorryName = ("customer name: "+customer_name), " " + ("Vehicle type = "+vehicle_type)
    current_vehicles.append(lorryName)
    cost_of_repair = new_lorry.fixVehicle()
    bill_repair.append(cost_of_repair)
    
