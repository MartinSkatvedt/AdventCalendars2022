import math

length = math.floor(math.pow(10, 5))


n_gifts = 0 #math.floor(math.pow(10, 6))
needed = 0
totalNeeded = 0
sledWeight = 1000
giftWeight = 0 
deer = 0

for i in range(length, 0, -1000):
    giftWeight += 1000

    needed = (giftWeight + sledWeight + deer * 100) / 200
    deer += needed


print(math.ceil(deer))


#1000 + 1000 + 0 / 200 = 10
#2000 + 1000 + 10 * 100 / 200 = 20
#3000 + 




