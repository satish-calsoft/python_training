
#d = input("enter value: ")
#d = 10
#for i in range(d+1):
    #c = i*'#'
    
    #e = c.center(50,' ')
    #print e    
############################
def Tri(userValue):
    dec = 10
    inc = 1
    for i in range(userValue):   
        if userValue <= 2:
            print dec*" "+inc*"* "
        elif i <= i < (userValue-1):
            print dec*" "+"* "+(2*i-2)*" "+"* "
        elif i == 1:
            print dec*" "+"* "+(2*i-1)*" "+"* "
        elif i == userValue-1:
            print dec*" "+inc*"* "
        dec = dec - 1
        inc = inc + 1        
           
Tri(8)    

#



