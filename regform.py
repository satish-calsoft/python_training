## passwd and cofnrm password must be same
# password length 8 ,one capital,one integr,one special char, week, fair,strong
# mobile number must have 10numbers
# firstname can not contain integers
#

def regform(**kargs):
    print kargs
    for i , j in kargs.iteritems():
        if kargs[i]:
            #print i
            if i == 'f_name':
                    if j.isalpha():
                        print "\nFirst Name: {}".format(j)
                    else:
                        print "\nplease give only char for {}".format(i)  
            if i == 'l_name':
                if j.isalpha():
                        print "\nLast Name: {}".format(j)
                else:
                        print "\nplease give only char for {}".format(i)
            if i == 'mobileno':
                #print 'hai'
                flag=True
                #print len(kargs[i])
                if len(kargs[i])==10:
                    #print len(kargs[i])
                    for x in kargs[i]:
                        #print "hai",x
                        if x not in '1234567890':
                            flag=False
                            if flag==False:
                                break
                    if flag:
                        pass
                    else:
                        print "\nplease give only digits for {}".format(i)
                else:
                    print "please give only 10 digits for {}".format(j)
                print "\nMobile no: {}".format(j)
                
                       
            if i =='username':
                if len(j)<4:
                    flag=0
                    print "username should conatin atleast 4 digits"
                elif j.isalpha() and j.isdigit():
                        print 'hai'
                else:                    
                        print "\nusername should contails chars and digits"
                print "\nUsername: {}".format(j)
            if i=='email':
                    if j.isspace():
                        print "please enter a valid email ID"
                    print "\nEmail ID: {}".format(j)
            if i=='password':
                if len(j)>=6:
                    if j.isalpha() and j.isdigit() and j.islower() and j.isupper():
                        if len(j)==6:
                            print "weak password"
                        elif len(j)>6 and len(j)<=8:
                            print 'good password'
                        elif len(j)>8:
                            print "stronge password"    
                else:
                    print 'password should contail 6 '
                    
                    
                
        else:
            print 'Please fill {}'.format(i)
            
        
def uvalid(j):
    return any(c.isdigit() for c in j)                   
        



#button=regform(f_name='chaitanya',l_name='ks',username='chaitu11',password='pwd123',confirm password='pwd123',mobile No='1234567890',email='123abc@xyz.com')
button=regform(f_name='chaitu',l_name='ks',username='chaitu1',password='pwd123',confirmpassword='pwd123',mobileno='9989994788',email='123abc@xyz.com')
#print button