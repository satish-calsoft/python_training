
l4 = [1, 2, 6, 2, 4, 9, 1, 3, 22, 19 , 6, 4, 8, 22]
#l4 = ['a', 'b', 'z', 'c', 'x']
l5 = []
l6 = [None] * len(l4)
for i in range(len(l4)):
    for j in l4:
        if l4[i] < j:
            l5.append('True')
        else:
            l5.append('False')
    x = l5.count('False')
    l6[x-1] = l4[i]
    l5 = []
    
for z in range(len(l6)):
    if l6[z] == None:
        l6[z] = l6[z+1]
    
        
print l6