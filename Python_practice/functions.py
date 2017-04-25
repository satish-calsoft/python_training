def sum1(a,b):
    
    return a+b,0,0

print sum1(1,2)



# Varable length arguments:if we pass an argument with * the type is tuple
def sum2(*a):
    print type(a)
    print a
    result = 0
    for i in a:
        print i
        result = result+i
    print result

sum2(3,4,5)
    