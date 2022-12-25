import csv
import pandas as pd
wheater = dict()

with open("vaer.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    wheater = {rows[0]:rows[1] for rows in reader}

col_data = []
with open("vannstand.txt", "r") as f:
    colIndex = 0
    lines = f.readlines()
    colLen = len(lines[0])
    while True:
        flag = True
        for index, line in enumerate(lines):
            if line[colIndex] != " ":
                col_data.append((index, line[colIndex]))
                colIndex += 1
                flag = False
                break
        if flag or colIndex >= colLen:
            break
    col_data.pop()

water_data = []
for i, col in enumerate(col_data):
    if i == 0:
        water_data.append((col[0], 0))
        continue
    if col[0] < water_data[i-1][0]:
        water_data.append((col[0], 1))
    elif col[0] > water_data[i-1][0]:
        water_data.append((col[0], -1))
    else:
        water_data.append((col[0], 0))


energyDict = {
(-1,"Mye regn"): 120_000,
(-1,"Lite eller ingen regn"): 100_000,
(0,	"Mye regn"): 80_000,
(0,	"Lite eller ingen regn"): 60_000,
(1,	"Mye regn"): 40_000
}

total = 0
for index, value in enumerate(water_data):
    if index == 0:
        continue
    if (value[1], wheater[str(index)]) in energyDict.keys():
        total += energyDict[(value[1], wheater[str(index)])]
    else:
        print("no")

print(total)