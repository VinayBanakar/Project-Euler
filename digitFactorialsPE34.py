def factorial(n):
    #print(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

li = []
for i in range(11,100000):
    sum =0
    x=i
    print('num ',x)
    while i > 0:
        sum += factorial(i%10)
        i = int(i/10)
    if sum == x:
        print('SUM: ',sum)
        li.append(sum)

print(li)