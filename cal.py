def sum(*args):
    result=0
    for i in range(len(args)-1):
        result=args[i]+args[i+1]
    return result
def sub(*args):
    result=0
    for i in range(len(args)-1):
        result=args[i]-args[i+1]
    return result
def mult(*args):
    result=0
    if 0 in args:
        return 0
    for i in range(len(args)-1):        
        result=args[i]*args[i+1]+result       
    return result
def square()


def inputs():
    
    ##if i != 'q' or 'Q':
        return none
print "enter values: "
result=0
x=input()
y=input()
print "enter operation(+,-,*,/):"
op=raw_input()
print x,y
if op == 'sum' or '+':
    #print 'hai'
    print " {} + {}: {}".format(x,y,sum(x,y))
if op == 'sub' or '-':
        print " {} - {}: {}".format(x,y,sub(x,y))

if op == 'mult' or '*':
            print " {} * {}: {}".format(x,y,mult(x,y))
