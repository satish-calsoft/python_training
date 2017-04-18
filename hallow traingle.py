a=input("enter value: ")
for i in range (a):
    if i==0:
        print '*'.rjust(a+1)
    elif i>=1:
        print (((' '.ljust(a-i)+'*'+(' '*(i+i-1))+'*')).rjust(a)).rjust(a+i)
        if i==a-1:
            print (('*'+' ')*(a+1))