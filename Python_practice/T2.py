
a=int(raw_input("Enter a value::"))
l1 =[]
i = 1

while i < a:
    l1 =l1+[i]
    i = i+1

#while i!= 0: 
#    l1 =l1+[i]
#    i = i-1

if i!= 0:
    l1 =l1+range(a,0,-1)
    
print l1
    
