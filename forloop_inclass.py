#l = []
#l1 = []

#for i in range(100):
    #if i % 2 == 0:
        #l.append(i)
    #else:
        #l1.append(i)

#print '{}\n{}'.format(l, l1)


##solution v2

#print 'Solution 2\n{}\n{}'.format(range(0, 100, 2), range(1, 100, 2))

##sol v3

#print 'Solution 3\n{}\n{}'.format([i for i in range(0, 100, 2)], [i for i in range(1, 100, 2)])


##Next Level

#ln1 = [1, 4, 2, 5, 7, 3]
#ln2 = [8, 1, 2, 5, 10, 11, 23]
#ln3 = []
#for i in ln1:
    #if i in ln2:
        #ln3.append(i)
        #print i
#print ln3

## Pythogrous theorm

## a^2 + b^2 = c^2
## 3^2 + 4^2 = 5^2


#lp1 = range(100)
#for i in range(len(lp1)):
    #if i + 2 <= len(lp1)-1:
        #if lp1[i]**2 + lp1[i+1]**2 == lp1[i+2]**2:
                #print [lp1[i], lp1[i+1], lp1[i+2]]

lp1 = range(50)

for i in lp1:
    for x in lp1:
        for y in lp1:
            if i**2 + x**2 == y**2:
                print i, x, y


