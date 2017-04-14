l1=[1,2,4,5,7,3]
l2=[8,1,2,5,10,11,23]
comml1=[]
for i in l1:
    #print i
    if i in l2:
        comml1.append(i)
print "Common elements are: ",comml1

for i in comml1:
    if i in l1 :
        l1.remove(i)
    if i in l2:
        l2.remove(i)
print "filtered lists {} {}: ".format(l1,l2)
    

        
#print l1

#""""for i in l2:
    
    #for i in l1:
        #l2.remove(i)
#print l2
