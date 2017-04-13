#!/usr/bin/python

list1=[1,4,2,5,7,3]
list2=[8,1,2,5,10,11,23]
Result=[]
for i in list1:
    for j in list2:
        if i==j:
            print i
            Result.append(i)

print "Common Numbers: ", Result
