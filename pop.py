#! /usr/bin/python
l1 = [9,8,7,6,5]
##l1.remove(l1[-1])  #1st solution to remove last index
print l1
i = input("enter index to remove from the list l1: ")
for j in range(len(l1)):
    
    if j==i:
        #l1.remove(j)
        del l1[j]
        
        print "After poping the index value: ",l1 # solution to remove the value using the index.

         
               
        
            


    
