
import math


R = 50
H = 160
L = math.sqrt(math.pow(R,2) + math.pow(H,2))

area = math.pi * R * L #area in cm^2
area = area / 100 #area in dm^2


red = area / 100 * 4 * 10
gold = area / 100 * 4 * 15
lights = area / 100 * 2 * 30
glitter = area / 100 * 5 * 15

total = red + gold + lights + glitter

print(total)

