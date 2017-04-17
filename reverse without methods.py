#! /usr/bin/python
list1 = [5,6,7,9,10]

count=0
for i in list1:
    count+=1
    
    
        
print count

for j in range(count/2):
       
    list1[j],list1[-j-1]=list1[-j-1],list1[j]
    print list1
        
#print list1




    
    
    
