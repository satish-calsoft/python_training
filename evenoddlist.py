#!/usr/bin/python
# for loops

leven=[]
lodd=[]
for i in range(101):
    if i%2==0:
        leven.append(i)
    
    else:
        lodd.append(i)
print "Odd number list\n",lodd
print "Even number list\n",leven


'''two lines of code
print range(0,101,2)
print range(1,101,2)'''





