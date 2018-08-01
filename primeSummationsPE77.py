def sievePrimeGen(start,end):
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

target=2
primes = sievePrimeGen(1,1000)

while True:
    ways = [0 for i in range(target+1)]
    ways[0] = 1

    for i in range(len(primes)):
        for j in range(primes[i],target+1):
            ways[j] += ways[j-primes[i]]
    if ways[target] > 5000:
        break
    target +=1
print("The first number written in over 5000 ways is",target)
#print(ways)