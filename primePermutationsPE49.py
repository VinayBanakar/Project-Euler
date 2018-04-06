import itertools, math
def seivePrimeGen(start, end):
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
        k += 1
    return primes

primeList = seivePrimeGen(1489,10000)
#print(primeList)

#Checks if two numbers given are permutations of each other. 
def arePerms(a,b):
    #Initial test to check if both the numbers dont have same lenght 
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
result =0
for i in range(0,len(primeList)):
    for j in range(i+1,len(primeList)):
        k = primeList[j]+ (primeList[j] - primeList[i])
        if k<10000 and k in primeList:
            print(primeList[i], primeList[j],k)
            if arePerms(primeList[i], primeList[j]) and arePerms(primeList[j], k):
                result = str(primeList[i])+str(primeList[j])+str(k)
                break
    if int(result) > 0:
        break
print(result)