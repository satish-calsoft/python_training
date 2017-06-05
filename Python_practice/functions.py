def sum1(a,b,c=5):
    
    return a+b+c

print sum1(1,2,3)

#ouput 6

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
    