x='*'
##Right Triangle
'''for i in range(0,5):
    print x*i'''
a=input("Enter the value: ")
for i in range(0,a):
    if i==0:
        print ' '*(a-i)+'*'
    elif i<a-1:
        print ' '*(a-i)+'*'+' '*i*2+'*'
    elif i==a-1:
        print ' '*(a-i)+'* '*(i+1)
        

    

