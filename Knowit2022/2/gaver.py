
gifts = []
with open("gaver.txt", "r", encoding="UTF-8") as f:
    gifts = f.readlines()

lines = 0
nGifts = 0

for gift in gifts:
    nGifts += 1
    lines += 2 + max(0, nGifts -3)
    
    if gift.find("alv") >= 0:
       nGifts -= 1 

print(lines)