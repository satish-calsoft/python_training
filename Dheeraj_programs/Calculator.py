num1 = input("Enter value for num1: ")
num2 = input("Enter value for num2: ")
choice = raw_input("Enter your choice(sum/sub/mul/div):")
if choice=="sum":
    print "the sum is : %d" %(num1 + num2)
elif choice=="sub":
    print "The difference is: %d" %(num1 - num2)
elif choice=="mul":
    print "The product is: %d" %(num1*num2)
elif choice=="div":
    print "The qotient is: %d" %(num1/num2)
