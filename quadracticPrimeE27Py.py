#sieve of eratosthenes [bigO(nloglogn)]
def sievePrime(limit):
    multiples = []
    primes = []
    for i in range(2,limit+1):
        if i not in multiples:
            print(i)
            primes.append(i)
            for j in range(i*i, limit+1, i):
                multiples.append(j)
    return primes

primes = sievePrime(87400)
print(primes)

def isPrime(num):
    global primes
    if num in primes:
        return True
    else:
        return False
print(isPrime(99))

aFin=0
bFin=0
nFin=0
for a in range(-1000,1001,1):
    for b in range(-1000,1001,1):
        n=0
        while isPrime(abs(n*n+a*n+b)):
            n+=1
        if n > nFin:
            aFin = a
            bFin = b
            nFin = n

print(aFin,bFin,nFin)

#brute force and bad 