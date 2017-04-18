length = input("Enter a no for length: ")
breadth = input("Enter a no for breadth: ")
char = raw_input("Enter Some symbol:")

for i in range(1,breadth+1):
    if i == 1 or i == breadth:
        print char.ljust(2)*length
    else:
        print char.ljust((length*2)-2)*2  