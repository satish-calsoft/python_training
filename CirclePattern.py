a=input("Enter the value: ")

for i in range(0,a):
    if i==0 or i==a-1:
        print ' '.rjust(8)+'* '*2
    elif i==1 or i==a-2:
        print ' '.rjust(4)+'*'+' '.rjust(8)+'* '
    elif i==3 or i==a-3:
        print ' '.rjust(2)+'*'+' '.rjust(12)+'* '
