import math
#generate pythagorean triplets by square sum relation 
c,m =0, 2
dit = {}
limits = 200
to_break = False
while not to_break:
 
    for n in range(1,m):
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        if c>limits:
        	if n == 1:
        		to_break = True
        if a+b+c in dit:
            dit[a+b+c] += 1
        else:
            dit[a+b+c] = 1
        print(a,b,c,a+b+c)
        #if a+b+c == 120:            
        #    print(a,b,c,a+b+c)
    m += 1
keylist=dit.keys()
sorted(keylist)
max,kio =0,0
for key in keylist:
    if max <= dit[key]:
        max = dit[key]
        kio = key
    print(key, dit[key])
print("==",kio,max)

#Looks like square sum relation does not generate all the triples.

def gcd(a,b):
    x,y= 0,0
    if a>b:
        x = a
        y = b
    else:
        x = b
        y = a
    while x%y != 0:
        temp = x
        x = y
        y = temp %x
    return y

a,b,c = 0,0,0
s = 1000
m,k,n,d=0,0,0,0
found = False

dit = {}
mLimit = int(math.sqrt(s/2))
for m in range(2,mLimit+1):
    if (s/2)%m==0:
        if m%2==0:
            k = m+1
        else:
            k = m+2
        while k<2*m and k<= s/(2*m):
            if s/(2*m) %k==0 and gcd(k,m)==1:
                d=s/2/(k*m)
                n = k-m
                a = d*(m*m-n*n)
                b = 2*d*n*m
                c = d*(m*m+n*n)
                found = True
                if a+b+c in dit:
                    dit[a+b+c] += 1
                else:
                    dit[a+b+c] = 1
                print(a,b,c,a+b+c)
                break
            k +=2
        if found:
            break

print(gcd(12,8))