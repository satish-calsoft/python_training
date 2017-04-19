l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,13]

for num1 in l1:
    for num2 in l2:
        if num1==num2:
            l1.remove(num1)
            l2.remove(num2)
            continue
        elif num1 != num2:
            continue
print "new l1 :", l1
print "new l2 :", l2
