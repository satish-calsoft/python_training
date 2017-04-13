#!/usr/bin/python
input1=input("Enter the first value: ")
input2=input("Enter the second value: ")
ArthimeticOperations=raw_input("Enter the Arthemetic Operator (Add,Sub,Mul,Div): ")

if ArthimeticOperations=="Add":
    print "Addition: ", input1+input2
    
elif ArthimeticOperations=="Sub":
    print "Subtraction: ", input1-input2
    
elif ArthimeticOperations=="Mul":
    print "Multiplication: ", input1*input2
    
elif ArthimeticOperations=="Div":
    print "Division:" ,div(input1,input2)
else:
    print "Invalid input"
    

