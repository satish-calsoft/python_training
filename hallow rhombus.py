a=input("enter value: ")
for i in range (a):
       if i==0:
              print '*'.rjust(a+a-1)
       else:
              print ('*'+' '*(i)+'*'+' '*(i)+'*').rjust(a+a+i)
for j in range (a,0,-1):
       if j==1:
              print '*'.rjust(a+a-1)
       elif j==a:
              print (('*'+' ')*(a+2)).rjust(a+a+a+1)
       else:
              print ('*'+' '*(j)+'*'+' '*(j)+'*').rjust(a+a+j)

              
        
    

        
