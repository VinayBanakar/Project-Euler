import math
#Pell's equation http://mathworld.wolfram.com/PellEquation.html

res,pmax = 0,0
pmax = 0

for D in range(2,1001):
    limit = int(math.sqrt(D))
    if limit * limit == D:
        continue 
    m,d,a = 0,1,limit
    num1,num = 1,a
    denm1,den = 0,1

    while num*num - D*den*den != 1:
        m = d*a-m
        d = (D-m*m)//d
        a = (limit+m)//d

        num2 = num1 
        num1 = num
        denm2 = denm1
        denm1 = den

        num = a*num1 + num2 
        den = a*denm1 + denm2
    
    if num> pmax:
        pmax = num 
        result = D

print(result)