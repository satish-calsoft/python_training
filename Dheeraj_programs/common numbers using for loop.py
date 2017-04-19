l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,13]
common_items = []

for i in l1:
    if i in l2:
        common_items.append(i)

print common_items
