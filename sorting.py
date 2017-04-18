lst=[1, 9, 8, 6, 1,2,5,3, 4]
for i in range(len(lst)):
            if i !=(len(lst)-1):
                        if lst[i]<=lst[i+1]:
                                    lst[i],lst[i+1]=lst[i+1],lst[i]
            
print lst
        