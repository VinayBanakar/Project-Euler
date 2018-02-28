import numpy as np

names = np.loadtxt("p022_names.txt", dtype="str" , delimiter=',')
names.sort()
totalScore = 0
ind=1
for i in names:
    k = i.lower()
    sum = 0
    for j in k:
        if j != '"':
            print(j,ord(j)-96)
            sum += ord(j)-96
    totalScore += (sum * ind)
    ind += 1
print(totalScore)