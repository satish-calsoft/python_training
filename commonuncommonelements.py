#!/usr/bin/python
l1=[1,4,2,5,7,3]
l2=[8,1,2,5,10,11,23]
l3=[]

for i in l1:
    for j in l2:
        if j==i:
            l3.append(j)
       
        
print "Common elements",l3

l1.extend(l2)
print l1

for j in l3:
    for k in l1:
        if j==k:
            l1.remove(j)
            

print l1

    



        
