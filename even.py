l =[1,2,3,4,7,9,0]
for i in xrange(100):
    if i%2 == 0:
        print i, "is even no" 
#########################################
a = []
b = []
def babu():
    for i in range(100):
        if  i%2 == 0:
            a.append(i)
        elif i%2 !=0:
            b.append(i)
    print a,"\n",b
babu()  
##############################################
evens = [i for i in xrange(100) if i%2 ==0]
print evens


