
#1>2 1>3 -> False add it to temp 
#2>1 2>3 -> False add it to temp
#3>1 3>2 -> True add it to c
#
#now make temp as original value,empty the list
#
#1>2 : False add it to temp
#2>1 : add it to c
#
#only one value add it to c

l1 = [9,1,2,3,5,4,10]
t1 = []
x = 0

while len(l1)!= 0:
    
    x = l1[0]
    
    for i in l1:
        
        if i < x:
            x = i
    t1.append(x)
    l1.remove(x)

print t1
            
        
        

  
    
    
        
   




        


    



    
    
    