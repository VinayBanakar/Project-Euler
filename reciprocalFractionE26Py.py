import math
from decimal import Decimal

def AS05(n):
    lpow=1
    while True:
        for mpow in range(lpow-1, -1, -1):
            if (10**lpow-10**mpow) % n == 0:
                return lpow-mpow
        lpow += 1 
max =0
ind = 0
def iterNum(n):
    global max, ind
    fact = prime_factors(n)
    print(fact)
    if 2 in fact or 5 in fact:
        if not set(fact) - {2,5}:
            print("not recurring not")
            return
        if not set(fact) - {2} or not set(fact) - {5}:
            print("not recurring not")
        else:
            print("reccuring")
            divideNum(n)
            tmp = AS05(n)
            print("len",tmp)
            if tmp > max: 
                max = tmp
                ind = n
    else: 
        print("recurring")
        tmp = AS05(n)
        print("len",tmp)
        if tmp > max: 
            max = tmp
            ind = n

def divideNum(n):
    x = Decimal(1)/Decimal(n)
    print(x)

def prime_factors(n):
    i=2
    factors=[]
    for i in range(2,n):
        while n% i ==0:
            n = n/i
            factors.append(i)
        if n==1:
            break
    if n > 1 : factors.append(n)
    return factors

for i in range(1,200):
    print(i, "===")
    iterNum(i)
print("Final max",max)
print("Final ind",ind)

#for any number n if the primefactor of n is equal 2^m * 2^n then 1/n is terminating. 
#For finding the number of repetitions: (10**x-10**y)mod(n) = 0 then x-y is the number of repetitions.