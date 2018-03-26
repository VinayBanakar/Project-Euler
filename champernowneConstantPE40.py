import string
a="0"
i=0
while 1:
    i+=1
    s=str(i)
    if len(a) <= 10**6:
        a+=s
    else: break

print(a)
def d(n):
    return int(a[n])
     
print(d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))