print(chr(65))
def WordScore(word):
    l = len(word)
    score=0
    for i in range(0,l):
        print(word[i],abs(64-ord(word[i])))
        score += abs(64-ord(word[i]))
    return score-60
li = open('p042_words.txt','r').read().split(',')
#li = ["POSTH","SBERB","SDBSDBRENERN","ERERBREEA"]
triangleNumbers = []
for k in range(1,1000000):
    y = 1/2*k*(k+1)
    triangleNumbers.append(int(y))
count=0
for i in li:
    sco = WordScore(i)
    print(i,sco)
    if sco in triangleNumbers:
        count += 1
print('count',count)