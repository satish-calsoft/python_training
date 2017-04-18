# display disctionary by converting two lists(one short& one long) and if values not sufficient then display value as "no value"
l=[1,2,3,4,5,6,7,8,9,10]
l1=['s','u','s','e']
d={}
for j in range(len(l)+1):
    for i in range(len(l1)):
        if j==i:
            d.update({l[j]:l1[j]})
        elif j>len(l1):
            d[j]='no value'
            
print d