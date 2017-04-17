l1=[1,4,2,5,7,3]
l2=[8,1,2,5,10,11,23,7]
l3=[5,1,7,11,10,99,13,15,3,3]
l4=[10,2,4,7,1,22,23,23,1,1,1,5]
Result=[]
'''for n in range(len(l4)):
    for i in l1:
        for j in l2:
            for k in l3:
                for l in l4:
                    if i==j==k==l:
                        Result.append(j)
print Result'''
'''for i in range(len(l1) and len(l2) and len(l3) and len(l4)):
    for j in (l1 and l2 and l3 and l4):
        if i==j:
            Result.append(i)

print Result'''
for i in l1:
    if i in l2 and i in l3 and i in l4:
        Result.append(i)

print Result
