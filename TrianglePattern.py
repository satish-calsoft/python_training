x='*'
##Right Triangle
#for i in range(0,5):
    #print x*i
a=input("Enter the value: ")
for i in range(0,a):
    if i==0:
        print ' '*(a+1)+'*'
    elif i<a-1:
        print ' '*(a-i)+'*'+' '*(i*2+1)+'*'
    elif i==a-1:
        #print ' '*(a-i)+'* '*(a+1)
        print ' '+(('*'+' ')*(a+1))

'''a=input("Enter the value: ")
for i in range(0,a):
    if i==0:
        print (' ').rjust(a+1)+'*'
    elif i<a-1:
        print (' ').rjust(a-i)+'*'+('  ').rjust(i*2+1)+'*'
    elif i==a-1:
        #print ' '*(a-i)+'* '*(a+1)
        print ' '+(('*'+' ')*(a+1))'''
        

    

