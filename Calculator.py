a= int(raw_input("Enter first number ="))
b= int(raw_input("Enter second number ="))

#choice of operator

d=int(raw_input("Enter your choice::\n1.Addition\n2.Suntraction\n"))
print d
if d==1:
    print "sum=%d" %(a+b)
elif d==2:
    print "difference=%d" %(a-b)
    
else :
    print "Choose the correct choice"
  