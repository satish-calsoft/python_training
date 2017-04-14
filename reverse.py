list = [1, 2, 3, 4, 5]
i = 0            
j = len(list)-1 
while i<j:
    list[i],list[j] = list[j],list[i]
    i += 1
    j -= 1
print list
