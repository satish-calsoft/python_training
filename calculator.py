import math
print("select operation")
print("1.add \n2.sub \n3.multiply \n4.divide \n5.x^y")

c = input("enter your choice(1/2/3/4/5): ")
num1 = int(input("enter first no: "))
num2 = int(input("enter second no: "))

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def x_pow_y(x,y):
    return int(math.pow(x,y))
#def sqroot(x):
    return math.sqrt(x)
if c == 1: print num1,"+",num2,"=",add(num1,num2) 
elif c == 2: print num1,"-",num2,"=",sub(num1,num2) 
elif c == 3: print num1,"*",num2,"=",mul(num1,num2)
elif c == 4: print num1,"/",num2,"=",div(num1,num2)
elif c == 5: print num1,"x^y",num2,"=",x_pow_y(num1,num2)
#elif c == 6: print "sqaureroot", num1,sqroot(num1)
else: print "invalid input"
