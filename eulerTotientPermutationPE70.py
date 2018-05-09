import math
from decimal import Decimal
def arePerms(a,b):
    #Initial test to check if both the numbers have same lenght 
    if int(math.log10(a)) != int(math.log10(b)) : return False
    aList = []
    bList = []
    aStr = str(a)
    bStr = str(b)
    for i in range(0,len(aStr)):
        #print("====",aStr[i],bStr[i])
        aList.append(int(aStr[i]))
        bList.append(int(bStr[i]))
    aList.sort()
    bList.sort()
    #print(aList,bList, aStr,bStr)
    if aList == bList:
        return True
    return False

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

best,phiBest,bestRatio = 1,1,float("Inf")
limit, lowerBound, upperBound = 10000000, 2000, 5000
primes = sievePrimeGen(lowerBound,upperBound)

for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        n = primes[i] * primes[j]
        if n>limit:
            break
        phi = (primes[i]-1)*(primes[j]-1)
        ratio = n/phi
        if arePerms(n,phi) and bestRatio > ratio:
            best =n
            phiBest = phi
            print(bestRatio,ratio)
            bestRatio = ratio

print("The perm with smallest ratio is ",best,"with fraction ", bestRatio)
