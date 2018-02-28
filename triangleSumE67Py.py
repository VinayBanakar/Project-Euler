import sys
d={}
def max_sum(i,j):
    if (i,j) in d:
        return d[(i,j)]
    if i==99:
        return a[i][j]
    d[(i,j)]=a[i][j]+max(max_sum(i+1,j),max_sum(i+1,j+1))
    return d[(i,j)]
a=[]
for i in range(100):
    b=list(map(int,sys.stdin.readline().split()))
    a.append(b)
print(max_sum(0,0))