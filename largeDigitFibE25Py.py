from decimal import Decimal
import math
import numpy as np
def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

def SubFib(startNumber, endNumber):
    for cur in F():
        print(cur)
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

ind =1
for i in SubFib(1, float('inf')):
    if(int(math.log10(i)+1) == 1000):
        print("I am ",i,"ind ",ind)
        break
    ind += 1

# n=5000
# while True:
   #  if(int(math.log10(fibgen(n))+1) == 1000):
#         print(n)
#         break
#     n += 1
