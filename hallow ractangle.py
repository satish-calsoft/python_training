a=input("enter value: ")
for i in range (a):
    if i==0 or i==a-1:
        print ('*'+' ')*(a+4)
    else:
        print '*'+('  ')*(a+2)+' *'
