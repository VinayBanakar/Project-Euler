val = 1
for i in range(100,1,-1):
    val *= i
print(val)
s = 0
while val:
    s += val%10
    val //= 10
print(s)
