value = input("enter your choice:")

for i in range(2,value):
    for j in range(2,i+1):
        if i>j and i%j == 0:
            break
        elif i>j and i%j != 0:
            continue
        elif j==i and i%j == 0:
            print i        