l1=[0,1,2,4,5,6,7,8,9]
l2=[10,11,12,13,14]
d = {}

'''for i in range(len(l1)):
    #d.get(l1[i],"no value")
    #d[l1[i]]=l2[i]
    for j in range(len(l2)):
        if i==j:
            d.update({l1[i]:l2[i]})
            break
        else:
            d.update({l1[i]: 'no value'})
    j=j+1
print d'''


for i in range(len(l1)):
    
        if i<len(l2):
            d[l1[i]]=l2[i]
        else:
            print l1[i], "has no value"
    
print d
