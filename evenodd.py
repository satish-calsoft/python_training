
even=[]
odd=[]
for i in range(100):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print "Even numbers below 100 are: {0} \nOdd numbers below 100 are: {1}".format(even,odd)
