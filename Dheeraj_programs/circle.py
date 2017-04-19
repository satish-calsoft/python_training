r = input("Enter radius: ")
a = input("Enter distance from line: ")
char = raw_input("Enter your choice: ")

for i in range(1,(r*2)+1):
    if i == 1 or i == (r*2):
        print ' '*(a+r),char.ljust(2)*2
    #elif i<r:
        #print ' '*(a+(r+i)),char.ljust((i*2)+2)*2
    elif i == r:
        print ' '*a,char.ljust(r+1)*3
    #elif i>r:
        #print ' '*a,char.ljust(i)*2