num = input("Enter value for num: ")
char = raw_input("Enter your choice:")

for i in range(1,num+1):
    if i == num or i == 1:
        print ' '*(num),char
    elif i<=(num/2):
        print ' '*((num+1)-i),char.ljust((i*2)-2)*2
    else:
        print " "*(i),char.ljust((num-i)*2)*2