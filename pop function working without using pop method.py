l=[1,2,6,3,4,5]
# 0 means last element remove and 1 means delete index according to your choice

a=input("enter which part you want to execute 0/1:")

if a==0:
    for i in l:
        if i==l[-1]:
            l.remove(i)
    print l 
else:
    n=input("which index value you want to delete:")
    c=0
    for i in l:
        c+=1
    #print c    
    for i in range(c):  
        if i==n:
            l.remove(l[i])
    print l
    




    
        

        