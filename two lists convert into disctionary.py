# two lists converts into disctionary
l=[1,2,3,4]
l1=['s','u','s','e']
d={}
for i in range(len(l)):
    d.update({l[i]:l1[i]})
print d
    
