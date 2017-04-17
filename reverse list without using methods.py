l=[3,4,6,8,9,5,7,1]
c=1
for i in l:
    c+=1
print c

for j in range(c/2):
        l[j],l[-j-1]=l[-j-1],l[j]
print l
    