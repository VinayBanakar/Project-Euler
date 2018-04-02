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
primeList = sievePrimeGen(100000)
def distinctPrimeFactors(numb):
    nod=0
    pf=True
    remain= numb
    for i in range(0, len(primeList)):
        if primeList[i]*primeList[i] > numb:
            nod += 1
            return nod
        pf = False
        while remain%primeList[i]==0:
            pf=True
            remain = remain/primeList[i]
        if pf:
            nod += 1
        if remain==1:
            return nod
    return nod

target = 4
consec = 4
finalConsec = 1
res = 2*3*5*7

while finalConsec < consec:
    res += 1
    if distinctPrimeFactors(res) >= target:
        finalConsec += 1
    else:
        finalConsec = 0

print(res-finalConsec+1)
