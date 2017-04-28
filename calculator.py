import math
l=[]
print 'Operations you will do in calculator addition/add, subtraction/sub, multiplication/mul, division/div, modulo/mod, xsquare, xcube, xpowery, squareroot, one by x, nfactorial/n!, ten power x, log, exponential/exp, sqrtxpower3, sqrtxpowery, sinh, cosh, tanh, sin, cos, tan'
a=raw_input("\n enter which operation you want to do in calculator: ")
if a.isupper() or a.islower() :
    if a=='add' or a=='a' or a=='addition':
        b=input("enter how many parameters you want to do addition:")
        for j in range (b):
            x=input("enter a value: ")
            l.append(x)
    
        def add(*a):
            result=0
            for i in l:
                result=result+i
            return result
        
        op=add(l)
        print op    
        
    elif a=='mul' or a=='m' or a=='multiplication':
        b=input("enter how many parameters you want to do multiplication:")
        for j in range (b):
            x=input("enter a value: ")
            l.append(x)
        def mul(*b):
            res=1
            for i in l:
                res=res*i
            return res 
        print mul(l)        
    
    elif a=='sub' or a=='subtraction':
        b=input("enter how many parameters you want to do subration:")
        for j in range (b):
            x=input("enter a value with sign: ")
            l.append(x)
        def sub(*b):
            r=0
            for i in l:
                r=r+i
                
            return r
        print sub(l) 
    
    elif a=='div' or a=='division':
        x=input("enter dividend value:")
        y=input("enter divisor value:")
        def div(a,b):
            z=a/b
            return z
        print div(x,y)  
    
    elif a=='modulo' or a=='mod':
        x=input("enter dividend value:")
        y=input("enter divisor value:")
        def mod(a,b):
            z=a%b
            return z
        print mod(x,y)   
    elif a=='xsquare' or a=='x square':
        x=input("enter a value you want to do sqaure: ")
        def xsquare(a):
            y=a**2
            return y
        print xsquare(x)
    elif a=='xcube' or a=='x cube':
        x=input("enter a value you want to do cube: ")
        def xcube(a):
            y=a**3
            return y
        print xcube(x)
    elif a=='xpowery' or a=='x power y' or a=='x^y':
        x=input("enter value of x:")
        y=input("enter value of y:")
        def xpowery(a,b):
            z=a**b
            return z
        print xpowery(x,y)          
    elif a=='sqrt' or a=='square root':
        x=input("enter a value you want to do sqare root: ")
        def sqareroot(a):
            y=math.sqrt(x)    
            return y
        print squareroot(x)  
    elif a=='onebyx' or a=='1 by x':
        x=input("enter x value: ")
        def onebyx(a):
            y=1/x
            return y
        print onebyx(x)
    elif a=='nfact' or a=='n factorial':
        x=input("enter n value: ")
        
        def fact(a):
            fact=1
            for i in range(1,a+1):
                fact=fact*i
            return fact
        print fact(x)
    elif a=='tenpowerx' or a=='10 power x' or a=='10^x':
        x=input("enter x value: ")
        def tenpowerX(a):
            y=10**a
            return y
        print tenpowerX(x)
    elif a=='sqrt x power y' or a=='sqrtxpowery':
        x=input("enter x value: ")
        y=input("enter y value: ")
        def sqrtxpowery(a,b):
            z=(math.sqrt(a))**b
            return z
        print sqrtxpowery(x,y)
    elif a=='sqrt x power 3'or a=='sqrtxpower3':
        x=input("enter a value: ")
        
        def sqrtxpowery(a):
            z=(math.sqrt(a))**3
            return z
        print sqrtxpowery(x)   

        
    elif a=='log':
        x=input("enter a value: ")
        def log(a):
            y=math.log(a)
            return y
        print log(x)
    elif a=='exp' or a=='exponential':
        x=input("enter a value: ")
        y=input("enter a value: ")
        def exp(a,b):
            z=a**b
            return z
        print exp(x,y)
    elif a=='sinh':
        x=input("enter a value: ")
        def sinh(a):
            y=math.sinh(a)
            return y
        print sinh(x)
    elif a=='cosh':
        x=input("enter a value: ")
        def cosh(a):
            y=math.cosh(a)
            return y
        print cosh(x)
    elif  a=='tanh':
        x=input("enter a value: ")
        def tanh(a):
            y=math.tanh(a)
            return y
        print tanh(x)
    elif  a=='sin':
        x=input("enter a value: ")
        def sin(a):
            y=math.sin(a)
            return y
        print sin(x)
    elif  a=='cos':
        x=input("enter a value: ")
        def cos(a):
            y=math.cos(a)
            return y
        print cos(x)
    elif  a=='tan':
        x=input("enter a value: ")
        def tan(a):
            y=math.tan(a)
            return y
        print tan(x)
        
else:
    print "its not a valid entry please select operation in above list"
    
    
    
    


    


        
    
    
    
    
        
        
          
    

        
    

    

    


    
    
    
