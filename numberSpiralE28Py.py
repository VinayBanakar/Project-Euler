import time
l = int(input("Length of Diagonal? "))
start_time = time.clock()
Sigma = 1 + 4*sum(4*k**2+k+3-2*((k+2)%(k+1)) for k in range(1, l+1))
# Tyalor Series
print(Sigma)
print(time.clock() - start_time, "seconds")

def f(x):
   return 16/3*x**3 + 10*x**2 + 26/3*x + 1 
start_time = time.clock()
print(f(l))
print(time.clock() - start_time, "seconds")
