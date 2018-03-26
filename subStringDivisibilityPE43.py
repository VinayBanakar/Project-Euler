from itertools import permutations
def checkIfPan(string):
    digits = len(string)
    if digits > 10:
        return False
    for i in range(0,digits):
        print(i,string)
        if str(i) not in string:
            return False
    return True

primeList = [2,3,5,7,11,13,17]
def bizareDivi(stringPan):
    track = False
    for k in range(1,8):
        numb = stringPan[k:k+3]
        #print(numb, stringPan)
        if int(numb) % primeList[k-1] == 0:
            track  = True
        else:
            return False
    return track
sum=0
for i in permutations('0123456789'):
    if i[0] == '0':
        continue
    n = ''.join(list(i))
    if bizareDivi(n):
        sum += int(n)
        print("====",n,sum)

