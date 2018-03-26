def panCheck(string):
    digits = len(string)
    if digits >= 10:
        return False
    for i in range(1,digits+1):
        if str(i) not in string:
            return False
    return True

import math
#simple primality check.
def checkIfPrime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        #print('i in',i)
        if n % i == 0:
            return False
    return True

max = 0
for i in range(12,100000000000000):
    if checkIfPrime(i):
        if panCheck(str(i)):
            if max < i:
                max = i
                print(max)

print(panCheck(str(12345)))