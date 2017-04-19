l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,23,7]
l3 = [5,1,7,11,10,99,13,15,3,3, ]
l4 = [10,2,4,7,1,22,23,23,1,1,1,5]

clist = []

                            
for i in l1:
    if i in l2 and i in l3 and i in l4:
        clist.append(i)

print clist