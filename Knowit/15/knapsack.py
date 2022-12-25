import csv
#value,volum

data = list()
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append((int(row[0]), int(row[1]))) 


trips = 0
maxW = 120
maxV = 1700

while data:
    value, volum = data.pop(0)

    for index, package in enumerate(data):
        if value + package[0] <= maxV and volum + package[1] <= maxW:
            value += package[0]
            volum += package[1]
            data.pop(index)

        if value == maxV or volum == maxW:
            break 
    trips += 1

print(trips)
