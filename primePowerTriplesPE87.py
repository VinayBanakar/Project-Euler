from itertools import product
def sievePrimeGen(limit):
    multiples=[]
    primes=[]
    for i in range(2,limit+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i,limit+1,i):
                multiples.append(j)
    return primes

# def another_sieve(n):
#     sieve = [True] * (n/2)
#     for i in xrange(3,int(n**0.5)+1,2):
#         if sieve[i/2]:
#             sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
#     return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

limit = 50000000
P = set()
for a,b,c in product(sievePrimeGen(7072), sievePrimeGen(369), sievePrimeGen(85)):
    q = a*a + b**3 + c**4
    if q >= limit: break
    P.add(q)
#print(P)
print(len(P))