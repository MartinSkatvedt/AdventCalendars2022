
import math


n = 5
controlBits = n+1
dataLen = math.pow(2, n) - controlBits

blocks = ""

with open("input.txt", "r") as f:
    startString = f.read()
    currentblock = ""
    for index, bit in enumerate(startString):
        currentblock += bit
        if len(currentblock) == 32:
            blocks += currentblock + " "
            currentblock = ""

print(blocks)
