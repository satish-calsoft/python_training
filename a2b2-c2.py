import math
a = range(1,5+1)
b = range(6,10+1)
c=[]
for i in a:
    for j in b:
        c = int(math.pow(i,2) + math.pow(j,2))
    print c