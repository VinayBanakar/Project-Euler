import time 

#Farey sequences https://en.wikipedia.org/wiki/Farey_sequence

start = time.time()
def fractionlessThan(ln,ld,rn,rd):
    return ln*rd < rn*ld

ln,ld = 0,1
rn,rd = 1,1
while ld +rd <= 1000000:
    mn = ln + rn
    md = ld + rd
    left = (mn==3 and md == 7) or not fractionlessThan(mn,md,3,7)
    if left:
        rn = mn
        rd = md
    else:
        ln = mn
        ld = md
end = time.time()
print("the fraction is :",mn,"/",md)