from garage import *

vehicle_type = print(" 1 = Car"'\n',"2 = Motorbike"'\n',"3 = Lorry")
new_vehicle = int(input("Enter vehicle choice:"))

if new_vehicle == 1:
    add_car()   
elif new_vehicle == 2:
    add_motorbike()
elif new_vehicle == 3:
    add_lorry()
    

append_list = (str(current_vehicles))
bill = (str(bill_repair))

list_file = open("vehicle_list.txt", "a")
bill_file = open("bill.txt", "a")
list_file.write(append_list + "\n")
bill_file.write(append_list + " Cost of repairs =" + bill + "\n")

bill_file.close
list_file.close()
vehicle_list = open("vehicle_list.txt", "r")

in_garage = vehicle_list.read()
print("Vehicles in garage = ",in_garage)
vehicle_list.close()












# car1 = Car(input("colour"), int(input("num")), int(input("num")), input("True"), int(input("num")), input("type"))
# car2 = Car("silver", 4, 12, False, 3, "mini")
# print("cost of repairs =",car1.fixVehicle())
# # print(car1.vehicleStatus())
# print("cost of repairs =",car2.fixVehicle())
# print(car2.vehicleStatus())

# bike1 = Motorbike("blue", 2, 8, True, True, True)
# bike2 = Motorbike("green", 2, 8, True, False, False)
# print("cost of repairs =",bike1.fixVehicle())
# print(bike1.vehicleStatus())

# print("cost of repairs =",bike2.fixVehicle())
# # print(bike2.vehicleStatus())

# lorry1 = Lorry("black", 18, 18, False, 4, 10)
# print("cost of repairs =",lorry1.fixVehicle())
# print(lorry1.vehicleStatus())







