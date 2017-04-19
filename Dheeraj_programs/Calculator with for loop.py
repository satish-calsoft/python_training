num1 = input("Enter value for num1: ")
num2 = input("Enter value for num2: ")
choice = ['sum','sub','mul','div']
#print "length of choice: %d" %(len(choice))
for i in choice:
    if i=="sum":
        print "the sum is : %d" %(num1 + num2)
    elif i=="sub":
        print "The differenc is: %d" %(num1 - num2)
    elif i=="mul":
        print "The product is: %d" %(num1*num2)
    elif i=="div":
        print "The remainder is: %d" %(num1/num2)
    else:
        print "Enter your choice again:"
