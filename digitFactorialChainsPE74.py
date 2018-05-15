def factorial(k):
    if k <1:   
        return 1
    else:
        retNumber = k * factorial( k - 1 ) 
        return retNumber
def factorialSum(num):
    toatalSum = 0
    numList = [int(d) for d in str(num)]
    for k in numList:
        toatalSum += factorial(k) 
    return toatalSum
def nonRepeatingChain(num):
    chain = []
    while num not in chain:
        chain.append(num)
        num = factorialSum(num)
    return chain
def countOfNonRepeating(num):
    return len(nonRepeatingChain(num))

limit = 1000000
count =0
nrNum = 60
for i in range(limit):
    if(countOfNonRepeating(i)==nrNum):
        count+=1

print(count,"number of chains bellow",limit,"conatin",nrNum,"non repeating terms")