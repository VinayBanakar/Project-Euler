import numpy as np

#matrix = np.loadtxt("test_table.txt", dtype='i', delimiter=',')
matrix = np.loadtxt("p082_matrix.txt", dtype='i', delimiter=',')
size = matrix[0].size
checked = []
print(matrix)
for i in range(0,size,1):
    checked.append(matrix[i][size - 1])
for i in range(size-2,-1,-1):
    checked[0] += matrix[0][i]
    for j in range(1,size,1):
        checked[j] = min(checked[j-1] + matrix[j][i], checked[j] + matrix[j][i])
    
    for j in range(size-2,-1,-1):
        checked[j] = min(checked[j],checked[j+1] + matrix[j][i])
print(checked)
checked.sort()
print("Sorted:",checked)