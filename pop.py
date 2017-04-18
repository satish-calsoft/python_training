list1=[3,2,4,7,5,6]
a=input("Enter the index to remove: ")
for i in range(len(list1)):
    if a==i:
        del(list1[i])
print list1

