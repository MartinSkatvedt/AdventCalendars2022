import re
from matplotlib import pyplot as plt
import numpy as np
from shapely.geometry import Polygon

xs = []
ys = []
S = []
pointOnHull = (float("inf"), 0)
    

with open("data.txt", "r") as f:
    for line in f.readlines():
        x = int(line.split(" ")[0])
        y = int(re.sub('\D', '', line.split(" ")[1]))
        xs.append(x)
        ys.append(y)
        if x < pointOnHull[0]:
            pointOnHull = (x, y)
        S.append((x, y))

P = []
i = 0


def isLeftOfLine(s_j, p_i, endp):
    return (endp[0] - p_i[0])*(s_j[1] - p_i[1]) > (endp[1] - p_i[1])*(s_j[0] - p_i[0])

while True:
    P.append(pointOnHull)
    endpoint = P[0]

    for j in range(0, len(S)):
       # plt.clf()
       # plt.scatter(xs, ys, color="blue")
       # x, y = zip(*P)
       # plt.scatter(x, y, color="green")
       # plt.plot(x, y, color="green")
       # plt.plot([P[i][0], S[j][0]], [P[i][1], S[j][1]], color="red")
       # plt.pause(0.001)
        if endpoint == pointOnHull or isLeftOfLine(S[j], P[i], endpoint):
            endpoint = S[j]
    i += 1
    pointOnHull = endpoint

    if endpoint == P[0]:
        P.append(P[0])
        break



pgon = Polygon(P)
print("Area: ",pgon.area)

plt.clf()
plt.scatter(xs, ys)
x, y = zip(*P)
plt.scatter(x, y, color="red")
plt.plot(x, y, color="red")
plt.show()
