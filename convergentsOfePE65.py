import math
limit,res = 100,0
d, n = 1,2

def digitSum(num):
    tmp,sum,remainder = num,0,0
    while tmp > 0:
        remainder = tmp % 10
        sum += remainder
        tmp = tmp - remainder
        tmp = tmp //10
    return sum

for i in range(2,limit+1):
    tmp = d
    if i % 3 ==0 :
        c = 2*(i//3)
    else:
        c = 1
    d = n
    n = c*d+tmp
res = digitSum(n)
print("The digit sum of numerator of 100th convergent is",res)