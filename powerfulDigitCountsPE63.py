import math
#formula from mathblog
# As we can tell 10^(n-1) <= x^n < 10^n 
# rewriting the expression we can find out that for lower bound: 
#       10^(n-1/n)<=x 
#And as n-1/n converges to 1 as it grows, the upper bound will be once lower crosses 10. 
res, low, n = 0,0,1

while low < 10:
    low = int(math.ceil(math.pow(10,((n-1)/n))))
    res += (10 - low)
    n += 1

print(res,n,low)