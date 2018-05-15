#Refer farey sequences. 
limit = 1000000
result = 0
phi = [n for n in range(limit+1)]
for i in range(2,limit+1):
    if phi[i] ==i:
        for j in range(i,limit+1,i):
            phi[j] = phi[j]//i * (i-1)
    result += phi[i]

print("Under a given denominator",limit,"there are",result,"proper fractions")