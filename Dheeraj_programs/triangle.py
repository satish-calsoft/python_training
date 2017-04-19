num = input("Enter value for num: ")
char = raw_input("Enter your choice:")

for i in range(1,num+1):
    if i==num:
        print char.ljust(2)*i
    elif i == 1:
        print ' '*((num-1)-i),char
    else:
        print " "*(num-(i+1)),char.ljust((i-1)*2)*2