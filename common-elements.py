#l3=[]
l1 = [1,4,2,5,7,3,100]
l2 = [8,1,2,5,10,11,23,100]
#for i in l1:
    #for j in l2:
        #if i ==j:
            #l3.append(j)
#print l3            
#############################
#l4 = []
#for a in l1:
    #if a in l2:
        #l4.append(a)
#print l4
############################
l5=[]
for a in l1:
    for b in l2:
        if a not in l2:
            l5.append(a)
        elif b not in l1:
            l5.append(b)
print l5
###############################
#l6=[]
#for a in l1:
    #if a not in l2:
        #l6.append(a)
#for b in l2:
    #if b not in l1:
        #l6.append(b)
#print l6
