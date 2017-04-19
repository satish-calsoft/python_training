num = input("Enter value for num: ")
char = raw_input("Enter your choice:")

for i in range(1,num+1):
    if i == 1 or i == num:
        print char.ljust(2)*num
    else:
        print char.ljust((num-1)*2)*2
