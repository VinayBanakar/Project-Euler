import calendar
count=0
for x in range(1901,2001):
    for y in range(1,13):
        if calendar.weekday(x,y,1)==1:
            print(x,y)
            count+=1

print(count)