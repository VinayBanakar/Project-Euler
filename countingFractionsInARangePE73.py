limit=12000
# Algo here https://en.wikipedia.org/wiki/Farey_sequence#Next_term
# a/b and c/d are adjacent if and only if bc-ad = 1, this is true for 1/3 and 4000/11999
a,b,c,d,=1,3,4000,11999
result = 0

while not (c==1 and d==2):
    result +=1 
    k = (limit+b)//d
    e  = k*c-a
    f = k*d-b
    a=c
    b=d
    c=e
    d=f

print(result)