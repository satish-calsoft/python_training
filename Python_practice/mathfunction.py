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

