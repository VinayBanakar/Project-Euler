def sievePrimeGen(limit):
    multiples=[]
    primes=[]
    for i in range(2,limit+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i,limit+1,i):
                multiples.append(j)
    return primes

def cumilativePrimeGen(prime):
    primeSum = []
    primeSum.append(0)
    for i in range(0,len(prime)):
        primeSum.append(primeSum[i]+prime[i])
    return primeSum

#Using cumulative sum of primes principle. 
limit=100000
res=0
numbOfPrimes=0
primeList = sievePrimeGen(limit)
#print(primeList)
primeSum = cumilativePrimeGen(primeList)

for i in range(numbOfPrimes,len(primeSum)):
    for j in range(i-(numbOfPrimes+1),-1,-1):
        if primeSum[i] - primeSum[j] > limit: break
        if primeSum[i]-primeSum[j] in primeList:
            numbOfPrimes = i-j
            res = primeSum[i]-primeSum[j]

print(res,numbOfPrimes)