#To comment seleced text ctrl+?
#To uncomment select text ctrl+shift+?

l1 = [1,4,2,5,7,3]
l2 = [8,1,2,5,10,11,23]
l3=[]
l4=[]

for i in l1:
    for j in l2:
        if i == j:
            print "common element",i
            l3.append(i)

       

print "Common elements:",l3

    
        

