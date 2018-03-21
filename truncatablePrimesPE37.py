import math
def isPrime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i ==0:
            return False
    return True

def truncRight(num):
    val = num % 10
    #num = int(num/10)
    st = str(num)
    num = int(st[:-1])
    return num
def truncLeft(num):
    val = num % 10
    #num = int(num/10)
    st = str(num)
    num = int(st[1:])
    return num
for i in range(100,120):
    print('=====',i)
    val = truncRight(i)
    print('a',val)
    print('b',truncRight(val))
    val = truncLeft(i)
    print('aL',val)
    print('bL',truncLeft(val))

#this is incomplete.