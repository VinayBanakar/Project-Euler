import math
def isPenta(numb):
    penta = (math.sqrt(1+24*numb) + 1.0)/6.0
    if penta == int(penta):
        #print(penta,int(penta))
        return True
    else:
        return False

res,i,k = 0,1,0
notFound = True
while notFound:
    i+=1
    n = i*(3*i-1)/2
    #print(n)
    for j in range(i-1,0,-1):
        m = j*(3*j-1)/2
        #print(n,m)
        if isPenta(n-m) and isPenta(n+m):
            res = n-m
            k=j
            notFound = False
            break

print("====",j,k,res)