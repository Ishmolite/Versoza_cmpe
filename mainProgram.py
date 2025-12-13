import os
import time
import csv

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) #mainProgram as root
print(BASE_PATH)
BASE_PATH2 = os.path.dirname(BASE_PATH) #mainProgram in sub folder

RESOURCE_PATH = os.path.join(BASE_PATH, "RESOURCES")
CSV_PATH = os.path.join(RESOURCE_PATH, "MYFIRSTCSV.csv")

csv_list_data = []

with open(CSV_PATH, mode = "r", newline ='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        csv_list_data.append(row)

print(csv_list_data)
print(csv_list_data[1])
print(csv_list_data[1][2])



'''Creating a new CSV file'''
name_and_address = []

for row in csv_list_data:
    name_and_address.append([row[1], row[4]])

CSV_PATH = os.path.join(RESOURCE_PATH, "NEWCSV.csv")

with open(CSV_PATH, mode = "w", newline ='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(name_and_address)






