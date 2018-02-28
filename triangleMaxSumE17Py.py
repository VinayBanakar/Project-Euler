import sys
def max_sum(i,j):
    if i==14:
        return a[i][j]
    return a[i][j]+max(max_sum(i+1,j),max_sum(i+1,j+1))
a=[]
for i in range(15):
    b=list(map(int,sys.stdin.readline().split()))
    a.append(b)
print(max_sum(0,0))