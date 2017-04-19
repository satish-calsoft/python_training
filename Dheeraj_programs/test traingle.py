num = input("Enter value for num: ")
char = raw_input("Enter your choice:")

for i in range(1,num+1):
    if i == num:
        print ' '*(num),char
    else:
        print " "*(i),char.ljust((num-i)*2)*2