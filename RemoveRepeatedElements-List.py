#!/usr/bin/python

list1=[1,4,2,5,7,3]
list2=[8,1,2,5,10,11,23]
Result=[]
list3=[]
#list1.extend(list2)
for i in list1:
    for j in list2:
        if i==j:
            print i
            Result.append(i)
    
print "Common Numbers: ", Result

list1.extend(list2)

print list1

for k in Result:
    for l in list1:
        if k==l:
            list1.remove(l)

print "Removed Repeated Elements ", list1
    
