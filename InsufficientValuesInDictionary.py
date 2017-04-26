l=[0,1,2,3,4,5,6,7,8,9]
l1=[10,11,12,13,14]
n=len(l1)
d={}
for i in range(len(l)):
    
    for j in range(n):
        
        if i==j:
            #print (i,j)
            d.update({l[i]:l1[j]})
            #print d
            break
        else:
            #print i
            d.update({l[i]:'No Values'})
            #print d
            
    j=j+1
print d
