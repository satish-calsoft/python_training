l1 = [1,4,2,5,7,3]
l2=  [8,1,2,5,10,11,23,7]
l3= [5,1,7,11,99,13,15,3,3]
l4= [10,2,4,7,1,22,23,1,1,1,5]
l5=[]

for i in l1:
    if i in l2 and i in l3 and i in l4:
        l5.append(i)
print l5
###################################
l6=[]
for i in l1:
    if i in l2:
        if i in l3:
            if i in l4:
                l6.append(i)
print l6      
######################################
l7 = []
for i in l1:
    if i not in l2:
        l7.append(i)
    elif l2 not in l1:
        l7 .append(l2)
    elif l3 not in l1:
        l7.append(l3)
print l7

