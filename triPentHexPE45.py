#Generate triangle numbes
triNum = []
for i in range(143,100000):
    x = i*(i+1)/2
    triNum.append(x)

#Generate Pentagonal numbers
pentNum = []
for i in range(143,100000):
    x = i*(3*i-1)/2
    pentNum.append(x)

#Generate hexagonal Numbers
hexNum = []
for i in range(143,100000):
    x = i*(2*i-1)
    hexNum.append(x)

temp = list(set(triNum).intersection(pentNum))
fin = list(set(temp).intersection(hexNum))

print(fin)