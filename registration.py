
def reg(**args):
    
    for k,v in args.items():
 #FirstName       
        if k == 'f_name':
            if v.isalpha():
                print "First name is valid:",v
            elif v == ' ':
                print ("First Name shoul not contain any spaces")
#Last Name
        if k =='l_name':
            if v.isalpha():
                print "Last name is valid: ",v
            if v == ' ':
                print ("Last Name Should not contain spaces ")
#User Name
        if k =='user_name':                 
            if len(v)>4 :
                print "User name is valid",v
            else:
                print "Username should be greater than 4characters"
            if v.isspace():
               print "Username Should not contain spaces"        
#Mobile Number       
        if k =='mob_num':
            if len(v)==10 and v.isdigit():
                print "Mobile number is valid",v
            else:
                print "Mobile Number is Not valid"
#EmailID
        if k == 'email':
            if v.__contains__('@' and '.com' or '.in'):
                print "email is valid",v
            else:
                print "Email is invalid"
#Password Verification
        if k== 'pwd':
            
            if len(v)==8:
                    print "Pwd is valid and strong",v
                
            elif len(v)>3<=7:
                    print "pwd is good"
            elif len(v)>1<=3:
                    print "pwd is bad"
            else:
                print "Password should npt exceed 8chars"
                
            for i in v:
                if i.isupper():
                    print "Password satisfied with uppercase letters"
                    break
                
               
            for j in v:
                if j.isdigit():
                    print "Password satisfied with numerical values"
                    break
                
            if v.__contains__('@' or '!' or '$' or '_'):
                print "Password satisfied with special characters"
            
            if v.isspace():
                print "Password should not contain spaces.So Password is invalid"
        
 #Confirm Password:
        if k == 'cpwd':
             if args['pwd']==v:
                print "Confirm Password Verified"
             else:
                print "Password Does Not Match."
            
        
  
    
        
    



print reg(user_name='JYOTHI',f_name=' ',l_name='jyo',pwd='Jyo1thi@',cpwd='jYyo1thi@',mob_num='12345',email='test@gmail.com')
