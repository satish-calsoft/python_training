num = input('Enter the number = ')
print num*" "+"*"
for i in range(1,num+1):
    print "%s*%s*" % ((num-i)*" ", ((i*2)-1)*" ")
print (num+1)*"* "