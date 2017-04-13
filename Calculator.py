print "Calculator\n"
int1=int(raw_input("Enter first value::"))
int2=int(raw_input("Enter second value::"))




choice1=int(raw_input("Select one operation to perform:\n1:Addition \n2:Subtraction\n3:Multiplication\n4:Divison\n"))
        
if choice1==1:
    print "Total=%d" %(int1+int2)
elif choice1==2:
    print "Total=%d" %(int1-int2)
elif choice1==3:
    print "Total=%d" %(int1*int2)
elif choice1==4:
    if int2==0:
        print "%d is not divisble by %d" %(int1,int2)
    else:
        print "Total=%d" %(int1/int2)
else:
    print "Select correct choice"
    
    