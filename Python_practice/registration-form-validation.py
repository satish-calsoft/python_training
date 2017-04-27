
def submit(**args):
    
            
    for i in args.keys():
        if (args[i] == "") and (i in manditory):
            print "username is mandatory field and it is empty"
            
        elif i == "pwd":
            if (args[i].isupper()) and (args[i].isnumeric() ):
                print "All the required characters exists"
            else:
                print "All the required characters not exists"
        
        elif i == "conf_pwd":
            if args[i] == args['pwd']:
                print "password and confirmation passwords are same"
            else:
                print "password and confirmation password  are not same"
        elif i == "f_name":
            if args[i].isalpha():
                print "first name is valid"
            else:
                print "first name is  not valid"
        elif i == "l_name":
            if args[i].isalpha():
                print "last name is valid"
            else:
                print "last name is not valid"
        elif i == "mob_no":
            
            if (args[i].isdigit()):
                print i,"is valid"
                if len(args[i]) != 10:
                    print "The length should be 10 digits"
            else:
                print i,"is not valid and it should be numbers"
                
        elif i == "email":
            
            if args[i].__contains__("@") and args[i].__contains__(".com"):
                print i,"valid email"
            else:
                print i,"Invalid email"
        

manditory =['u_name', 'conf_pwd', 'pwd', 'email', 'mob_no']
submit(u_name ="",pwd = "@saibb", conf_pwd = "A1@saibb",f_name = "",l_name = "raju",mob_no = "12345678",email = "abc")

