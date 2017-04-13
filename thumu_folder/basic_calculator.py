num1 = input("enter a digit: ")
num2 = input("enter a digit: ")


operation = input("\n1. Addition \n2. Subtraction \n3. Multipication \n4. Division \nEnter the number for the operation to perform:  ")


if operation == 1:
    print "addition"
    print num1+num2
elif operation == 2:
    print "Subtraction"
    print num1-num2
elif operation == 3:
    print "Multiplicaiton"
    print num1*num2
elif operation ==4:
    print "Division"
    print num1/num2



