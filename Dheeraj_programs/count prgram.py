#l = [1,2,3,4,1,1,2,2,3,4,4,2,3,1]
s = ['a','b','c','d']
a = 0
for i in s:
    for a in range(s.index(i)):
        a = a+1

print a