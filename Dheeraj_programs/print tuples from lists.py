a = [1,2,3,4,5]
b = ['m','n','o','p','q']

for i in a:
    for j in b:
        if a.index(i) == b.index(j):
            print (i,j)
            