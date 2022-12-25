import re
import math



def getInfoFromString(line):
    splitLine = line.split(",")
    temp = splitLine[1].split(" ")[2]
    water = splitLine[2].split(" ")[2]
    gas = splitLine[3].split(" ")[2]

    values = [temp, water, gas]
    returnValues = []
    for value in values:
        returnValues.append(int(re.sub('\D', '', value)))

    returnValues.append(splitLine[0]) 
    return returnValues

def calcSoda(machineInfo):
    sodaProduced = 0
    if machineInfo[0] >= 95 and machineInfo[0] <= 105 and machineInfo[1] >= 400 and machineInfo[1] <= 1500 and machineInfo[2] >= 300 and machineInfo[2] <= 500:
        waterUsed = machineInfo[1] - 100
        gasUsed = machineInfo[2]/10
        
        sodaProduced = math.floor(waterUsed + gasUsed)
        if machineInfo[0] >= 100:
            sodaProduced -= math.floor((sodaProduced/40))

    return sodaProduced


total = 0
mostProducedValue = 0
mostProducedMachine = ""
allMachines = []
with open("julebrusmaskiner.txt", "r") as f:
    for maskin in f.readlines():
        machineInfo = getInfoFromString(maskin)
        machineInfo.append(calcSoda(machineInfo)) 
        allMachines.append(machineInfo)


machineDict = dict()
for index, machine in enumerate(allMachines):
    current = machineDict.get(machine[3])
    if current == None:
        machineDict.update({machine[3] : machine[4]})
    else:
        machineDict.update({machine[3]: current+machine[4]})

print(machineDict)
total = 0
for machine in machineDict.items():
    total += machine[1]

    if machine[1] > mostProducedValue:
        mostProducedValue = machine[1]
        mostProducedMachine = machine[0]
print(total, mostProducedMachine)
