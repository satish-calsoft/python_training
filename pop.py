#! /usr/bin/python
l1 = [1,5,2,8]
##l1.remove(l1[-1])
print l1
l=len(l1)
i = input("enter index to remove: ")
for j in range(l):
    if j==i:
        l1.remove(j)
    
print "After poping the index value: ",l1

               
               
        
            


    
