l=[0,1,2,3,4,5,6,7,8,9]
l1=[10,11,12,13,14,15,16]
x={}
for i in range(len(l1)):
    if len(l1)<=len(l):
        x[l1[i]]=l[i]
        print x  
    else:
    print x.setdefault(i,None)
