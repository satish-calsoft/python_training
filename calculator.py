print("select operation")
print("1.add")
print("2.sub")
print("3.multiply")
c = input("enter your choice(1/2/3): ")

num1 = int(input("enter first no: "))
num2 = int(input("enter second no: "))

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
if c == 1:
    print num1,"+",num2,"=",add(num1,num2) 
elif c == 2:
    print num1,"-",num2,"=",sub(num1,num2) 
elif c ==3:
    print num1,"*",num2,"=",mul(num1,num2)
else:
    print "invalid input"