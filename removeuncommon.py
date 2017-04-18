#remove common elements from the lists 
new=[]
l1=[1,4,2,5,7,3]
l2=[8,1,2,5,10,11,23]
for i in l1:
    for j in l2:
        if i==j:
            new.append(i)
for i in new:
    if i in l1:
        l1.remove(i)
print l1

for i in new:
    if i in l2:
        l2.remove(i)
print l2

# actual version

l1=[1,4,2,5,7,3]
l2=[8,1,2,5,10,11,23]
for i in l1:
    for i in l1:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
print l1,"\n",l2

        
                
    








        
        
        
        