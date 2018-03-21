def panCheck(string):
    digits = len(string)
    if digits >= 10:
        return False
    for i in range(1,digits+1):
        if str(i) not in string:
            return False
    return True

def concat(a,b):
    c = b
    while c > 0:
        a *= 10
        c /= 10
    return a+b
result = 0
for i in range(9387,9233,-1):
    result = concat(i,2*i)
    print(result)
    if panCheck(str(result)):
        break
print(result)