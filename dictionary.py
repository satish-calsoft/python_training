l=[0,1,2,3,4,5,6,7,8,9]
l1=[10,11,12,13,14,15,16,17,18,19]
d={}
for i in range(len(l1)):
    d.update({l[i]:l1[i]})
    
print d

