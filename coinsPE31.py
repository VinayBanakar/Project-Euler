import time 
coin = 200
ways = 0
start_time = time.clock()
#Brute force
for i in range(200,-1,-200):
    for j in range(i,-1,-100):
        for k in range(j,-1,-50):
            for l in range(k,-1,-20):
                for m in range(l,-1,-10):
                    for n in range(m,-1,-5):
                        for o in range(n,-1,-2):
                            ways += 1
print(ways)
print(time.clock()-start_time," Seconds")

#Dynamic programming
coins = [1,2,5,10,20,50,100,200]
ways = [0] * 201
print(ways)
ways[0]=1
for i in range(0,len(coins),1):
    for j in range(coins[i],coin+1,1):
        ways[j] += ways[j-coins[i]]
print(ways)