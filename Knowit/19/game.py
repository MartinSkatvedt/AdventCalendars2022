
import math
from typing import List


class Tyv:
    position = None
    nextGoal = None
    finalGoal = None
    route = None
    effect = None
    hasMovedhalf = False
    count = 0

    def __init__(self, route):
        self.position = [0,0]
        self.route = route
        self.finalGoal = self.route[-1]
        self.nextGoal = self.route.pop(0)
    
    def isAtCurrentGoal(self) -> bool:
        return (self.position[0] == self.nextGoal[0]) and (self.position[1] == self.nextGoal[1])
    
    def moveToGoal(self):
        x = self.nextGoal[0] - self.position[0]
        y = self.nextGoal[1] - self.position[1]

        moveVec = [0, 0]
        if y > 0:
            moveVec[1] += 1
        elif y < 0:
            moveVec[1] -= 1
        if x > 0:
            moveVec[0] += 1
        elif x < 0:
            moveVec[0] -= 1

        if self.effect == 'A':
            if (self.position[0] == 0 and self.position[1] == 0):
                moveVec = [0,0]
            else:
                moveVec[0] *= -1
                moveVec[1] *= -1
            
            self.count -= 1
            if self.count == 0:
                self.effect = None

        elif self.effect == 'S':
            if not self.hasMovedhalf:
                self.hasMovedhalf = True
                moveVec = [0, 0]
            else:
                self.hasMovedhalf = False
            self.count -= 1
            if self.count == 0:
                self.hasMovedhalf = False
                self.effect = None

        
        self.position[0] += moveVec[0]
        self.position[1] += moveVec[1]

        if self.isAtCurrentGoal() and (len(self.route) > 0):
            self.nextGoal = self.route.pop(0)
    
    def isAtFinalGoal(self) -> bool:
        return self.position[0] == self.finalGoal[0] and self.position[1] == self.finalGoal[1]
    
    
distDict = {
    'A': 10,
    'L': 10000,
    'S': 5
}

cdDict = {
    'A': 2,
    'L': 4,
    'S': 2
}

class Cannon:
    position = None
    type = None
    dist = None
    cooldown = 0

    def __init__(self, pos, type):
        self.position = pos
        self.type = type
        self.dist = distDict[self.type]
    
    def thiefInRange(self, thief: Tyv) -> bool:
        return math.sqrt(math.pow(thief.position[0] - self.position[0], 2) + math.pow(thief.position[1] - self.position[1], 2)) <= self.dist
    
    def canFire(self, thief: Tyv) -> bool:
        if (not self.thiefInRange(thief)) or (thief.effect != None) or (self.cooldown > 0):
            return False
        else:
            return True
    
    def fire(self):
        self.cooldown = cdDict[self.type]



route = [[8,0],[8,12],[22,12],[22,4],[32,4],[32,22],[20,22],[20,36],[44,36],[44,24],[58,24],[58,48],[82,48]]
cannons = [('L',12,30),('A',6,8),('S',24,10),('A',28,12),('A',24,26),('S',18,32),('A',34,34),('S',48,28),('S',60,28),('S',56,36)]

thieves = []
with open("input.txt", "r") as f:
    curr = ""
    for letter in f.readlines()[0]:
        if letter == 'T':
            thieves.append("T")
        else:
            thieves.append("")
            
#route = [[4,0],[4,7],[8,7],[8,3],[11,3],[11,14],[20,14]]
#cannons = [('L',2,13),('S',5,5),('A',9,9)]

t_obj = []
cannons_in_play: List[Cannon] = []

def distToGoal(thief: Tyv):
    return math.sqrt(math.pow(route[-1][0] -thief.position[0], 2) + math.pow( route[-1][1]- thief.position[1], 2))


for n in thieves:
    curr = []
    for i in range(0, len(n)):
        curr.append(Tyv(route.copy()))
    t_obj.append(curr)

for n in cannons:
    type = n[0]
    pos = [n[1], n[2]]
    cannons_in_play.append(Cannon(pos, type))

thieves_in_play: List[Tyv] = []
tick = -1
flag = True
while flag:
    tick += 1
    if (len(t_obj) > 0):
        thieves_in_play += t_obj.pop(0)

    thieves_in_play.sort(key = lambda x: distToGoal(x))
    for thief in thieves_in_play:
        removed = False
        for cannon in cannons_in_play:
            if cannon.canFire(thief):
                if cannon.type == 'L':
                    thief.effect = 'L'
                    thieves_in_play.remove(thief)
                    removed = True
                elif cannon.type == 'A':
                    thief.effect = 'A'
                    thief.count = 2
                elif cannon.type == 'S':
                    thief.effect = 'S'
                    thief.count = 6
                cannon.fire()
                break

        if not removed:
            thief.moveToGoal()
            if thief.isAtFinalGoal():
                flag = False
                print("Thief at goal, at tick:", tick)
                break

        
    for cannon in cannons_in_play:
        if cannon.cooldown > 0:
            cannon.cooldown -= 1
