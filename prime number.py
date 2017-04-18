# find prime number in a given range

a=[]
num= input("Enter the number =")
for i in range (2,num):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        a.append(i)

print a
