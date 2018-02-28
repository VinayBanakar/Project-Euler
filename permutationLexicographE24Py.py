#using itertools 

from itertools import permutations

l = list(permutations(range(0,10)))
l.sort()
val = 1000000-1
print(l[val])
print(len(l))

