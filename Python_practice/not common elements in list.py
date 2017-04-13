l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,23]
l3 = []
#1 in l2:yes
#4 in l2:no
#2 in l2:yes

for i in l1 :
    if  i in l2:
        continue
    else:
        l3.append(i)
for i in l2:
    if i in l1:
        continue
    else:
        l3.append(i)

print "l1=",l1
print "l2=",l2
print "l3=",l3

l4=l1+l2
l5=[]
for k in l4:
    if k in l1 and k in l2:
        continue
    else:
        l5.append(k)
print "l5=",l5