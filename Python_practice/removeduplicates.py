l1 = [1,1,1,1,1,2,2,2,2]
k = 0
#for i in l1:
#    for j in l1[1:]:
#        if i==j:
#            print "inside=i,j=",i,j
#            l1.remove(j)
#            print "inside loop",l1
#    print "outside=i,j",i,j        
#    print "outside loop =",l1  
#print l1




i = 0
l1 = [1,1,1,2,2,2,3,4,4,4,5,5,5,5,5]
while i < len(l1)-1:
    
    
    if l1[i] == l1[i+1]:
        l1.pop(i)
    else:
        i = i+1

print l1


    