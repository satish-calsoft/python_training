# find even number 

a=[1,2,3,4,5,6,7,8,9,0]
#for i in a:
    #if i % 2 == 0:
        #print i, "is a an even number"
    #else:
        #print i, "is an odd number"
        
        
## range (find even numbers in a range of 100)

#a= range (101)
#for i in a:
    #if i % 2 == 0:
        #print i, "is an even number"
    #else:
        #print i, "is an odd number"
        
## print even and odd number in range
        
#print range (0,100,2)
#print range (1,100,2)

## use for loop 

#even=[]
#odd=[]
#for i in range (100):
    #if i % 2 == 0:
        #even.append(i)
    #else:
        #odd.append(i)
#print even
#print odd
      

# find common elements among given lists
common=[]
uncommon=[]
l1=[1,4,2,5,7,3]
l2=[8,1,2,5,10,11,23]
for i in l1:
    for j in l2:
        if i==j:
            common.append(i)
        
print common

#