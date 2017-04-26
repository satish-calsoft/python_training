def add(a,b=0,*more):
    result=0
    result=a+b+more[0]+more[1]
    print a,b
    print "arbitary: ",more
    return result

#d = add(2,4)
print add(2,4,6,7)

add.__doc__

def kargs(**args):
    sum=0
    print args
    for i ,j in args.items():
        sum=sum+j
    return sum

f=kargs(a=3,b=2)
print f