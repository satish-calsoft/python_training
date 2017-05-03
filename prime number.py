a = input("enter range:")
s=[]
for i in range(2,a):
    for j in range(2,i+1):
        if i %j==0 and i>j:
            break
        elif i==j and i%j==0:
            s.append(i)
        else:
            continue
print s
        