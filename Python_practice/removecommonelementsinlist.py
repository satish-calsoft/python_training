l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,23]
l3 = []

for i in l1:
  for j in l2:
    if i == j:
      print "common element",i
      l3.append(i)


for i in l3:
  if i in l1 and l2:
    l1.remove(i)
    l2.remove(i)
print l1,l2