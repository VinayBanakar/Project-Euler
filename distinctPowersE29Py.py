se = set([])
li = []
for i in range(2,10):
    for j in range(2,10):
        se.add(i**j)
        li.append(i**j)
print(len(se))
li.sort()
print(li)
