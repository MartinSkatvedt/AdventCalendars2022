import math
import time

start = time.time()
n = 1

while True:
    n += 1
    if n % 2 != 0:
        continue

    if math.pow(2, 13) % (n-1) == 1:
        exact = True
        for i in range(1, 13):
            if math.pow(2, i) % (n-1) == 1:
                exact = False
                print(n, "will be ready by", i)
                break

        if exact:
            print(n)
            break
        else:
            continue
end = time.time()

elapsed_time = end - start
print('Execution time:', elapsed_time, 'seconds')