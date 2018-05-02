#brute force is bad: it would be rediculous to generate figurate numbers of triangle, square, hex, etc
#and do comparisions and rotations. But let me write an eficient brute force method :p

import sys
# Generates figurate numbers 
def generateFigurateNumbers(type):
    numbers=[]
    n, number = 0,0
    while number<10000:
        n += 1
        if type == 0:
            #Triangle numbers
            number = n * (n+1)/2 
        elif type ==1:
            #Square numbers
            number = n*n
        elif type == 2:
            #Pentagonal numbers 
            number = n* (3*n -1)/2
        elif type ==3:
            #Hexagonal numbers
            number = n*(2*n -1)
        elif type ==4:
            #Heptagonal numbers
            number = n*(5*n-3)/2
        elif type == 5:
            #Octatgonal numbers 
            number = n*(3*n - 2)
        if number > 999 and number < 10000:
            numbers.append(number)
    return numbers

result = sys.maxsize
solution = [0 for i in range(6)]
numbers = []

#Find next in the chain. 
def findNext(last, length):
    for i in range(len(solution)):
        if solution[i] != 0:
            continue
        for j in range(len(numbers[i])):
            unique = True
            for k in range(len(solution)):
                if numbers[i][j] == solution[k]:
                    unique = False
                    break
            if unique and ((numbers[i][j]/100) == (solution[last]%100)):
                solution[i] = numbers[i][j]
                print(solution)
                if length == 5:
                    if solution[5]/100 == solution[i]%100: 
                        return True
                if findNext(i,length+1):
                    return True
        solution[i] = 0
    return False

for i in range(6):
    numbers.append(generateFigurateNumbers(i))
for i in range(len(numbers[5])):
    solution[5] = numbers[5][i]
    if findNext(5,1):
        break 
result = sum(solution)

print(numbers)
print(solution)
print(result)

#failed :/ 

