l1,l2,comm=[1,2,4,5,7,3],[8,1,2,5,10,11,23],[]
for i in l1:
    if i in l2:        comm.append(i)
for i in comm:
    if i in l1 and i in l2 :
        l1.remove(i)
        l2.remove(i)
print "filtered lists {} {}: ".format(l1,l2)