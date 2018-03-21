import math
#simple primality check.
def checkIfPrime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        #print('i in',i)
        if n % i == 0:
            return False
    return True

#this method rotates the digit by one. 
def rotator(num):
    le = len(str(num))
    print(le)
    la = num % 10
    ret = str(la) + str(num//10)
    return ret

pol =[]
for i in range(11,1000000):
    k=2
    if checkIfPrime(i):
        print(i)        
        z =i
        y = len(str(i))
        while k <= y:
            Track = False
            i = rotator(int(i))
            if checkIfPrime(int(i)):
                Track = True
            else:
                break
            print("i ",i)
            k += 1
        if Track:
            pol.append(int(z))
print(sorted(set(pol)))
print(len(set(pol))+4)