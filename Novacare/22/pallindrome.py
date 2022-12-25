def isPallindrome(number):
    strNumb = str(number)
    return strNumb == strNumb[::-1]

def isPrime(n): # from https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

total = 17740683
for n in range(1908580, 0, -1):
    numb = n
    counter = 0
    if int(str(n)[-1]) != 7:
        continue
    while True:
        if isPallindrome(numb):
            break


        if counter == 2000:
            if str(numb)[0:4] == "1337":
                total += n
                print(n, total)
            break
        
        numb += int(str(numb)[::-1])
        counter += 1

print(total)



