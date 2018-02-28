import numpy as np
input = np.loadtxt("p081_matrix.txt", dtype='i', delimiter=',')
#input = np.loadtxt("test_table.txt", dtype='i', delimiter=',')
print(input)
size = input[0].size
for i in range(size-2,-1,-1):
    #print(input[size-1][i],input[size-1][i+1])
    #print(input[i][size-1], input[i+1][size-1])
    input[size-1][i] += input[size-1][i+1]
    input[i][size-1] += input[i+1][size-1]
print(input)

for i in range(size-2,-1,-1):
    for j in range(size-2,-1,-1):
        #print(input[i][j])
        input[i,j] += min(input[i+1][j], input[i][j+1])
        #print(input[i][j])

print(input)
#A clasic DP problem