l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,13]
other_list = []

for num1 in l1:
    if num1 not in l2:
        other_list.append(num1)
for num2 in l2:
    if num2 not in l1:
        other_list.append(num2)

print other_list