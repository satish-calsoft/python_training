# find uncommon elements among given lists

uncommon=[]
l1=[1,4,2,5,7,3]
l2=[8,1,2,5,10,11,23]
for i in l1:
    if i not in l2:
        uncommon.append(i)
for i in l2:
    if i not in l1:
        uncommon.append(i)
print uncommon
        
    
            

