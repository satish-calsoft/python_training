print "CALCULATOR\n"
import math

def value():
    
    while 1:
        
        int1 =input("Enter a number to perform operation::")
        backspace = raw_input("BP to remove the value:")
        if backspace == "BP":
            int1 = 0
        else:
            break 
    return int1

def plus(i,result):
    
    result = result + float(i)
    return result

def minus(i,result):
    
    result = result - float(i)
    return result

def multi(i,result):
    
    result = result * float(i)
    return result

def div(i,result):
    
    result = result / float(i)
    return result

def sqrt(result):
    
    return math.sqrt(result)

def power(i,result):
    
    return math.pow(result,i)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)



result = float(value())

while 1:
    
    op1 = raw_input("Choose a option::\n 1.Addition \n 2.Subtraction  \n 3.Multiplication \n 4.Divison \n  5.sqrt \n 6.pow(x,y) \n 7.sin  \n 8.cos \n 9.tan  \n 10.Result  " )
    
    if op1 == "1":
        
        int1 =value()
        result = plus(int1,result)
        
        print result
    elif op1 == "2":
        int1 =value()
        result = minus(int1,result)
        print result
        
    elif op1 == "3":
        int1 =value()
        result = multi(int1,result)
        print result
        
    elif op1 == "4":
        while 1:
            int1 =value()
            if int1 == 0:
                print "value not divisible by 0"
            else:
                result = div(int1,result)
                print result   
                break
            
    elif op1 == "5":
        
        result = sqrt(result)
        print result
        
    elif op1 == "6":
        int1 =value()
        result = power(int1, result)
        print result
    
    elif op1 == "7":
        
        result = sin(result)
        print result
          
    elif op1 == "8":
        
        
        result = cos(result)
        print result
        
    elif op1 == "9":
        
        
        result = tan(result)
        print result    
             
        
    elif op1 == "10":
        print "result=",result
        break
    
    
    else:
        print "Select correct option::"
    