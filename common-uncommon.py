list1 = [1, 4, 2, 5, 7, 3]
list2 = [8, 1, 2, 5, 10, 11, 23]
list3 = list1+list2
commonlist = []
uncommonlist = []
for i in list1:
    for j in list2:
        if j==i:
	    commonlist.append(j)
        
for l in commonlist:
    for k in list3:
	if l == k:
	    list3.remove(k)
print "uncommon elements", list3          
print "Common elements", commonlist

