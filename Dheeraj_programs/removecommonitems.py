l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,13]

for i in l1:
    for i in l1:
        if i in l2:
            l1.remove(i), l2.remove(i)

print l1, "\n", l2
