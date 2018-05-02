import math

#Wiki link for algorithm https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
limit =10000
res = 0

for i in range (2,limit+1):
    curLimit = int(math.sqrt(i))
    if curLimit * curLimit == i:
        continue
    period,d,m,a, = 0,1,0,curLimit
    while True:
        m = d*a - m
        d = (i-m*m)//d
        print(i,m,d,res)
        a = (curLimit+m)//d
        period += 1
        if a == 2*curLimit:
            break
    if period % 2 ==1:
        res += 1
print("Square roots with odd period below ", limit," is ", res)
