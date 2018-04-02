import math
#this overflows and gives wrong answer. 
def returnSelfSqureSum(limit):
    tmp = 0
    for i in range(1,limit+1):
        tmp += i**i
        #print(i,i,i**i)
    return tmp

print(returnSelfSqureSum(1000))
#clo = str(returnSqureSum(1000))
#print(clo[:-10])

##########
#Modulo solution for the question
res = 0
mod = 10000000000
for i in range(1,1001):
    temp = i
    for j in range(1,i):
        temp *= i 
        temp %= mod
    
    res += temp
    res %=mod

print(res)
