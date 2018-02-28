from math import sqrt; from itertools import count, islice
import time
start_time = time.time()
amicList = {}
finalList = set([])
index =0

def isPrime(n):
         return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def getEvenSum(n):
    evenSum = 0
    for r in range(1,n):
        if n%r == 0:
            evenSum += r
    return evenSum

for i in range(4,10000,1):
    if not isPrime(i):
        sum = getEvenSum(i)
        print(i,sum)
        if sum > i:
            x = getEvenSum(sum)
            print(sum,x)
            print("==")
            if x == i and i != sum:
                finalList.add(i)
                finalList.add(sum)
finSum = 0
for i in list(finalList):
    finSum += i
print(finalList)     
print(finSum)
print("--- %s seconds ---" % (time.time() - start_time))
#This needs memoization, bad complexity here. 

        
        