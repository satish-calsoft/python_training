#collection of disimilar items--List
#collection of similar items--Array

l=[1,'a',2]
print dir(l)
l.append(4)
l.append([1,4,5])
print l
l1=[2,3,4]
l.extend(l1)
print l
b="abc"
l.extend(b)
print l
print l[0]
a=10
l3=[a]
print l3
print l
l.insert(2,'a')
print l
l.insert(2,l3)
print l
print l.index('a')
print l.pop(5)
l.reverse()
print l
l.sort()

