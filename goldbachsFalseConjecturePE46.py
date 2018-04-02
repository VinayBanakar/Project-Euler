import math
#Goldbach's wrong conjecture
primeList = []
def sievePrimeGen(limit):
    multiples=[]
    primes=[]
    for i in range(2,limit+1):
        if i not in multiples:
            print(i)
            primes.append(i)
            for j in range(i*i, limit+1,i):
                multiples.append(j)
    return primes

def isGoldbach(numb):
    for prime in primeList:
        if prime < numb:
            x = math.sqrt((numb-prime)/2)
            print(numb,prime,x)
            if x == int(x):
                print(True)
                return True
        else:
            return False
    return False
    
primeList = sievePrimeGen(6000)
for i in range(5,6000,2):
    if i not in primeList:
        if isGoldbach(i):
            # print(i,True)
            continue
        else:
            print(i, False)
            break 