import math
from matplotlib import pyplot as plt

r_max = math.pow(10, 6)
alpha = 0.2
gamma = 7.5 * math.pow(10, -5)
delta = 83
beta = 0.1


r_0 = 125000
u_0 = 3500

def U_calc(r, u):
    return math.floor(u + (gamma * u * r)/(delta) - beta*u)

def R_calc(r, u):
    return math.floor(r + (alpha * r*(r_max - r))/(r_max) - (gamma*u*r))


n_max = int(math.pow(10, 6))

U = [3500]
R = [125000]

xs = []
ys = []
for n in range(1, n_max + 1):
    u = U_calc(r_0, u_0)
    r = R_calc(r_0, u_0)


    u_0 = u
    r_0 = r
    R.append(r_0)

    xs.append(n)
    ys.append(r_0)
print(r, u)

#plt.plot(range(0, n_max+1), R, color="blue")
#plt.plot(range(0, n_max+1), R, color="red")
#plt.show()

