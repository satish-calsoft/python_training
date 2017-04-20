#Manditory arguments

def sum1(a,b):
   
    return a+b
print sum1(2,3)

#optional arguments

def sum1(a,b=0):
   
    return a+b
print sum1(2,3)

#variable length arguments
# *a represents parameters in tuple 

def sum1(*a):
    result=0
    print a
    for i in a:
        result=result+i
    return result
print sum1(3,4)

# **a keyword arguments represents dictionary




