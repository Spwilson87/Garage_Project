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






