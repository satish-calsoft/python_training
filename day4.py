l1 = [1, 5, 6, 9, 4]
l2 = [2, 4, 2, 6, 7]


for i in range(len(l1)):
    lr = l1[i], l2[i]
    print lr



#common elements in given lists.
    
l1 = [1, 4, 2, 5, 7, 3]
l2 = [8, 1, 2, 5, 10, 11, 23, 7]
l3 = [5, 1, 7, 11, 10, 99, 13, 15, 3, 3, ]
l4 = [10, 2, 4, 7, 1, 22, 23, 23, 1, 1, 1, 5]
l5 = []
for i in l1 + l2 + l3 + l4:
    if i in l1 and i in l2 and i in l3 and i in l4:
        if i not in l5:
            l5.append(i)
print l5

