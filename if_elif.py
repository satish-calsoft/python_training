#if,elif, else condition

a = raw_input("Enter a first number: ")
b = raw_input("Enter a second number: ")

if a < b:
    print "Value %r is small" %a 
elif a > b: 
    print "Value %r is big" %a
elif a == b:
    print "%r and %r values are same" %(a, b)
    
else: 
    print "Please enter only numbers"
    
    