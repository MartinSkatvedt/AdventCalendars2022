import numpy as np

def isPalindrome(number):
    return number == number[::-1]

total = 0

for i in range(1, 10000000):
    pal_counter = 0
    for base in range(2, 17):
        if isPalindrome(np.base_repr(i, base)):
            pal_counter += 1
        
        if pal_counter >= 3:
            total += i
            break

print(total)