#key must be unique
#key must be immutable data type(string,int,tuple)

#d[4]=1
#d
#{3: 1, 4: 1}

#d.update({1:20,6:7})
#d
#{1: 20, 3: 1, 4: 1, 6: 7}

#d.get(1)
#20
#d.get(20)



#d.setdefault(8)
#d.setdefault(8,2)
#d
#{1: 20, 3: 1, 4: 1, 6: 7, 8: None}
#d.setdefault(8,"s")
#d
#{1: 20, 3: 1, 4: 1, 6: 7, 8: None}
#d.setdefault(9,"ad")
#'ad'
#d
#{1: 20, 3: 1, 4: 1, 6: 7, 8: None, 9: 'ad'}
#d.setdefault(10,2)
#2
#d
#{1: 20, 3: 1, 4: 1, 6: 7, 8: None, 9: 'ad', 10: 2}


#l = [0,1,2,3,4,5,6,7,8,9]
#l1  = [10,11,12,13,14,15,16,17,18,19]
#l2 = {}
#
#j = 0
#
#if len(l) > len(l1):
#        diff =len(l)-len(l1)
#        for i in range(diff):
#                
#        
#
#for i in l :
#        l2[i] = l1[j]
#        j = j+1
#        
#print l2


i ={1:1,2:1}
print i.keys()
print i.values()
print i.items()
print i.get(2)
print i.pop(2)
print i 
i.setdefault(3,4)
print i 
i.clear()
print i 
i ={1:1,3:4,5:7}
j=i.copy()
print i,j
print id(i),id(j)
print i.has_key(0)
i.popitem()
print i,j
print i.viewitems()
print i.viewkeys()
print i.viewvalues()

d1 = i.iteritems()
print d1
print d1.next()
print d1.next()

d2 = i.iterkeys()
print d2
print d2.next()
print d2.next()


d3 = i.itervalues()
print d3

print d3.next()
print d3.next()

print i

for l,m in i.items():
    print l,m