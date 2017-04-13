#Logic 1
list1 = [1,4,2,5,7,3]
list2 = [8,1,2,5,10,11,23]
list3 = []

for i in list1 :
    if  i in list2:
        continue
    else:
        list3.append(i)
for i in list2:
    if i in list1:
        continue
    else:
        list3.append(i)

print "list3=",list3

#Logic 2

list4=list1+list2
list5=[]
for k in list4:
    if k in list1 and k in list2:
        continue
    else:
        list5.append(k)
print "list5=",list5