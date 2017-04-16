l1 = [1,2,3,4,5]
l2 = []
i=0

for k in l1:
    i = i+1
    l2 = l2 + [k]
print l2   
f=i
j = 0
while j < i:
    
    l2[j] = l1[f-1]
    j = j+1
    f = f-1
    
print "Reverse list:",l2



    
    

    