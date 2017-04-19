num = input("Enter value for num: ")
char = raw_input("Enter your choice:")

#for i in range(1,num+1):
    #if i==num:
        #print char.ljust(2)*i
    #elif i == 1:
        #print ' '*((num-1)-i),char
    #else:
        #print " "*(num-(i+1)),char.ljust((i-1)*2)*2


# for printing characters two times the given value
for i in range(1,(num*2)+1):
    if i==(num*2):
        print char.ljust(2)*i
    elif i == 1:
        print ' '*((num*2)-(i+1)),char
    else:
        print " "*((num*2)-(i+1)),char.ljust((i-1)*2)*2