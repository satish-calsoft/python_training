print "CALCULATOR\n"
import math

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



result = float(input("Enter a number :"))

while 1:
    
    op1 = raw_input("1->+   2->-   3->*  4->/  5->=sqrt 6->pow(x,y) 7->sin 8->cos  9->tan   10->= \n " )
    
    if op1 == "1":
        int1 =input("Enter a number to perform operation::")
        result = plus(int1,result)
        
        print result
    elif op1 == "2":
        int1 =input("Enter a number to perform operation::")
        result = minus(int1,result)
        print result
        
    elif op1 == "3":
        int1 =input("Enter a number to perform operation::")
        result = multi(int1,result)
        print result
        
    elif op1 == "4":
        while 1:
            int1 =input("Enter a number to perform operation::")
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
        int1 =input("Enter a number to perform operation::")
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
    