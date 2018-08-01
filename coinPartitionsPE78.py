# https://en.wikipedia.org/wiki/Partition_(number_theory)
p = []
p.append(1)

n = 1
while True:
    i,penta=0,1
    p.append(0)
    while penta <= n:
        sign =0
        if i%4 > 1:
            sign = -1
        else:
            sign = 1
        #print(n,p[n], penta, sign,p)
        p[n] += sign * p[n-penta]
        p[n] %= 1000000
        i += 1

        j = 0
        if i%2==0:
            j = i//2+1
        else:
            j = -(i//2+1)
        penta = int(j*(3*j-1)//2)
    if p[n]==0:
        break
    n += 1

print(n)
    