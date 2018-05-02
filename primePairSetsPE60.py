import itertools as iter 
import random
def seivePrimeGen(start,end):
    multiples=[]
    primes=[]
    for i in range(2,end+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i,end+1,i):
                multiples.append(j)
    k=0
    while True:
        if primes[k]>start:
            primes = primes[k:]
            break 
        k+=1
    return primes 

size = 5
primes = seivePrimeGen(0,10000)

def createChain(chain):
    if len(chain)== size:
        return chain
    for p in primes:
        if p > chain[-1] and arePriemes(chain+[p]):
            newChain = createChain(chain+[p])
            #print(newChain)
            if newChain:
                return newChain
    return False 

def isPrime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

def arePriemes(chain):
    return all(isPrime(int((str(p[0]) + str(p[1])))) for p in iter.permutations(chain, 2))

chain = 0
while not chain:
    chain = createChain([primes.pop(0)])

print("Sum of 5 primes", sum(map(int, chain)), chain)
