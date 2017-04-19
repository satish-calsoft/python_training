#to create a dic with two lists
#l=range(10)
#l1=range(10,20)
#d={}
#for i in range(len(l)):
    #d[l[i]]=l1[i]
#print d

##Squares
#l=range(10)
#d={}
#for i in range(len(l)):
    #d[l[i]] = l[i] * l[i]
#print d 

##to form a dic with 10keys and 5 values
l=range(10)
l1=range(10,15)
d={}
for i in range(len(l)):
    if i < len(l1):
        d[l[i]]=l1[i]
    else:
        print (str(l[i]) + 'has no value') 
print d        
            
          
       