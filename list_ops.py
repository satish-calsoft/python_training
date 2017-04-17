l1=[3,4,2,1,8]
l2=[21,32,45,67,99]
tuplst=[]
for i in range(len(l1)):
    t=l1[i],l2[i]
    print t
    tuplst.append(t)

print tuple(tuplst)


