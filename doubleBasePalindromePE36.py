def isPalindrome(num):
    st = str(num)
    rev = ''.join(reversed(st))
    if st == rev:
        return True
    return False

pol=[]
sum=0
for i in range(1,1000000):
    print(i,bin(i)[2:])
    if isPalindrome(i) and isPalindrome(bin(i)[2:]):
        sum += i
        pol.append(i)

print(pol)
print(sum)