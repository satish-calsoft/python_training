print "CALCULATOR\n"
import mathfunction 



result = float(mathfunction.value())

while 1:
    
    op1 = raw_input("Choose a option::\n 1.Addition \n 2.Subtraction  \n 3.Multiplication \n 4.Divison \n  5.sqrt \n 6.pow(x,y) \n 7.sin  \n 8.cos \n 9.tan  \n 10.Result  " )
    
    if op1 == "1":
        
        int1 =mathfunction.value()
        result = mathfunction.plus(int1,result)
        
        print result
    elif op1 == "2":
        int1 =mathfunction.value()
        result = mathfunction.minus(int1,result)
        print result
        
    elif op1 == "3":
        int1 =mathfunction.value()
        result = mathfunction.multi(int1,result)
        print result
        
    elif op1 == "4":
        while 1:
            int1 =mathfunction.value()
            if int1 == 0:
                print "value not divisible by 0"
            else:
                result = mathfunction.div(int1,result)
                print result   
                break
            
    elif op1 == "5":
        
        result = mathfunction.sqrt(result)
        print result
        
    elif op1 == "6":
        int1 =mathfunction.value()
        result = mathcunftion.power(int1, result)
        print result
    
    elif op1 == "7":
        
        result = mathfunction.sin(result)
        print result
          
    elif op1 == "8":
        
        
        result = mathfunction.cos(result)
        print result
        
    elif op1 == "9":
        
        
        result = mathfunction.tan(result)
        print result    
             
        
    elif op1 == "10":
        print "result=",result
        break
    
    
    else:
        print "Select correct option::"
    