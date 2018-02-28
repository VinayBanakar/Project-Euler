#using itertools 

from itertools import permutations

l = list(permutations(range(0,3)))
l.sort()
print(l)