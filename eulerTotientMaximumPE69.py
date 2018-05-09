# Returns a count of relative primes with the given num.
def totient(num):
    count=0
    for i in range(1,num):
        if gcd_euclid(i,num)==1 :
            count += 1
    return count

def gcd_euclid(a,b):
    if a==0:
        return b
    return gcd_euclid(b%a,a)

def nonIntuitive():  
    limit=1000001
    maxim,val,num = 0,0,0
    for k in range(2,limit):
        val = k//totient(k)
        if val > maxim:
            num =k
            maxim = val
    print("The number with max n/phi(n) under ",limit-1," is ",num," with value ",maxim)

def sievePrimeGen(start,end):
    multiples=[]
    primes=[]
    for i in range(2,end+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i,end+1,i):
                multiples.append(j)
    k=0
    while True:
        if primes[k]>start:
            primes = primes[k:]
            break 
        k+=1
    return primes 

# https://en.wikipedia.org/wiki/Euler's_totient_function
def euler_totient_func():
    result,i,limit=1,0,1000000
    primes = sievePrimeGen(1,200)
    while (result*primes[i]) < limit:
        result *= primes[i]
        i+=1
    print("The number with max n/phi(n) under ",limit," is ",result)

# more efficient
euler_totient_func()

#compute intensive
#nonIntuitive()

######################################################
# phi here is the above totient function
# Some phi rules:
# * phi(p) = p-1, if p is a prime number.
# * phi(pq) = (p-1)(q-1) = phi(p) * phi(q) # in RSA encryption.
# * phi(p^k) = p^k - p^(k-1) while k>0
# * if m and n are coprime then, phi(mn) = phi(m)*phi(n)

# Finally these give raise to Eulers Theorem:
#   if gcd(a,n) = 1, a^phi(n) congruent to 1(mod n)
######################################################
