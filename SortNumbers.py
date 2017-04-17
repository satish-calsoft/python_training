list1=[3,2,4,7,5,6]
result=[]
for i in range(len(list1)):
    a=min(list1)
    result.append(a)
    list1.remove(a)
print result
    
'''for i in range(len(list1)):
    for j in list1:
        if j<list1[-i-1]:
            result.append(j)
print result'''
            
