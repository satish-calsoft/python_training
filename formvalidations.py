########### first all fields must be have date########
##########Next validate all fields##############
 
#c = {"u_name":"ravi","l_name":"babu", "passwd":"tehelka", "mob_no":283982983, "email":"abc@gmail.com"}
import re
def _submit(**args):
    print args.keys()
    for v in args.keys():
        
        if v in ["u_name","passwd","mob_no"]:
            if " " in args[v]:
                print v,"****enter value*****"
        
        if v == "u_name":
            if " " in args[v]: print "****enter valid username****"
            else: print "valid username"
            
        if v == "passwd":
            pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$"
            result = re.findall(pattern, args[v])
            if (result): print "Valid passwd"
            else: print "*******Invalid passwd enter correct one*******"
        
        if v == 'mob_no':
            if args[v].isdigit():
                print "valid mobile no"
            else:
                print "******Enter valid mobile no******"
        
        if v == "email" and args["email"]:
            if "@" in args[v] and ".com" in args[v]:
                print "Valid Email"
            else:
                print "********Enter Valid Email*******"
                
        if v == "l_name" and args["l_name"]:
            if  not args[v].isalpha() or  " " in args[v]: print "******Enter valid last name*********"
            else: print "Valid Last name"
       
_submit(u_name= "Ravi", l_name = "raja", passwd = "teheLk@1", mob_no="23982983", email = "abc@gmail.com ")

