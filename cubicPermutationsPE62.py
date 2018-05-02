digits = ''
minCube = float('Inf')
n = 100
minNum = 5
cubes = {}

while minCube == float('Inf') or len(digits) <= len(str(minCube)):
    c = n*n*n
    digits = ''.join(sorted(str(c)))
    if digits in cubes:
        cubes[digits] += [c]
        if len(cubes[digits]) == minNum:
            minCube = min(minCube, cubes[digits][0])
    else: 
        cubes[digits] = [c]
    n += 1
print(minCube)