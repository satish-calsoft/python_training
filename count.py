a=[2,2,4,3,3,5,6,8,8,9,0,0,1,4,1,2]
unique_elements = []
for i in a:
    if i not in unique_elements:
        unique_elements.append(i)
for j in unique_elements:
    count = 0
    for i in a:
        if j==i:
            count=count+1
    print "count of ",j,"is : ",count
          
          
    