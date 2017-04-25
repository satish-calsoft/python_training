print "Calculator\n"
import  math
def add1(x,y):
    
    return x+y
    
def sub1(x,y):
    
    return x-y

def mul1(x,y):
    
    return x*y

def div1(x,y):
    
    return x/y

def power1(x,y):
    return x**y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)



choice1=int(raw_input("Select one operation to perform:\n1:Addition \n2:Subtraction\n3Multiplication\n4:Divison\n5.xpowery\n6.squareroor\n"
                      "7.sin\n8.cos\n9.tan\n"))
        
if choice1==1:
    
    int1=int(raw_input("Enter first value::"))
    int2=int(raw_input("Enter second value::"))    
    print "int1+int2=",add1(int1,int2)
    
elif choice1==2:
    int1=int(raw_input("Enter first value::"))
    int2=int(raw_input("Enter second value::"))    
    print "int1-int2=",sub1(int1,int2)
    
elif choice1==3:
    
    int1=int(raw_input("Enter first value::"))
    int2=int(raw_input("Enter second value::"))    
    print "int1*int2=",mul1(int1,int2)
elif choice1==4:
    
    int1=int(raw_input("Enter first value::"))
    int2=int(raw_input("Enter second value::"))
    
    if int2==0:
        print "%d is not divisble by %d" %(int1,int2)
    else:
        print "int1/int2=",div1(int1,int2)
        
elif choice1==5:
    
    int1=int(raw_input("Enter first value::"))
    int2=int(raw_input("Enter second value::"))    
    print "xpowery=",power1(int1,int2)
    
elif choice1==6:
    
    int1=int(raw_input("Enter a value::"))
    print "sqrt(int1)=",sqrt(int1)
    
elif choic1==7:
    
    int1=int(raw_input("Enter a value::"))
    print "sin(int1)=",sin(int1)
    
elif choic1==8:
    
    int1=int(raw_input("Enter a value::"))
    print "cos(int1)=",cos(int1)

elif choic1==9:
    
    int1=int(raw_input("Enter a value::"))
    print "tan(int1)=",tan(int1)
    
else:
    print "Select correct choice"
    
    