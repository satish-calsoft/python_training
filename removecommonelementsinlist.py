l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,23]
print "l1=",l1
print "l2=",l2
for i in l1:
    for j in l2:
        if i == j:
            l1.remove(i)
            l2.remove(j)
            
print "l1=",l1
print "l2=",l2