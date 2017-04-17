from math import sqrt
a = input("enter range:")
for i in range(1,a):
    for j in range(i,a):
        k = i**2 + j**2
        c = int(sqrt(k))
        if (k==c**2):
            print(i, j, c)