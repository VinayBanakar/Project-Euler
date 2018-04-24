import copy
import random

def percentOfPrimes(totalPrimes, n):
    return totalPrimes/ ((n-1)*4 +1 )

n=2 
currentCorner = 9
totalPrimes = 3

#Primality check. 
def rabinMiller(num):
    # Returns True if num is a prime number.
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


while percentOfPrimes(totalPrimes,n) > 0.1:
    n += 1
    for i in range(4):
        currentCorner = currentCorner + (n-1)*2
        if rabinMiller(currentCorner):
            totalPrimes += 1

print(2*n-1)