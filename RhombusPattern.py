a=input("Enter the value: ")
for i in range(a):
    
    if i==0:
        print ' '*(a+1)+' *'
    elif i<a/2:
        print ' '*(a-i)+'*'+' '*(i+1)+'*'+' '*(i+1)+'*'
    elif i==a/2:
        print ' '*(a-i)+'* '*(i+3)

for j in range(a,-1,-1):
    
    if j == 0:
        print ' '*(a+1)+' *'
    elif j<a/2:
        print ' '*(a-j)+'*'+' '*(j+1)+'*'+' '*(j+1)+'*'
    #elif j==a/2:
        #print ' '*(a-j)+'* '*(j+3)
