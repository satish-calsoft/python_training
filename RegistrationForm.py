def submit(**args):
    for key,value in args.items():
        if key=='f_name':
            if value.isalpha():
                print "FirstName is valid: ", value
            else:
                print "FirstName has no data"
                
        if key=='l_name':
            if value.isalpha():
                print "LastName is valid: ", value
            else:
                print "LastName has no data"
        if key=='mobile':
            if value.isdigit() and len(value)==10:
                print "Mobile number is valid", value
            else:
                args[key]=raw_input("Enter the valid mobile number: ")
        if key=='username':
            if value.isalpha() and len(value)>4:
                print "UserName is valid: ", value
            else:
                print "Please provide username with minimum lenght of four characters"
                args[key]=raw_input("Enter the username: ")
        if key=='password':
            if len(value)==8:
                print "Password Strength is GOOD"
            elif len(value)>9<15:
                print "Password Strength is FAIR"
            elif len(value)>15:
                print "Password Strength is Excellent"
            else:
                args[key]=raw_input("Password Strength should be minimum of 8 characters. Please improve the password strength: ")
            for i in value:
                if i.isupper():
                    print "Password is statisfied with uppercase letter"
                    break
                
            for j in value:
                if j.isdigit():
                    print "Password is satisfied with integer"
                    break
                

            if value.__contains__('@'or'$'or'&'or'_'):
                pass
            else:
                print "Password should contain special characters"
            if value.isspace():
                print "Password should not contains spaces"


        if key=='confirmpassword':
            #print key
            #print args['password']
            if value==args['password']:
                
                print "Confirm password matches with the password"
            else:
                args[key]=raw_input("Your confirm password doesnt match with your password. Please provide it again: ")
        if key=='email':
            print key
            if value.__contains__('@') and value.__contains__('.com'):
                print "Email ID is valid: ", value
            else:
                args[key]=raw_input("You have entered invalid email id. Please provide the valid email id: ")


print submit(f_name='sindhu',l_name='guturu',user_name='sindhugss',password='Sindhu@123',confirmpassword='Sindhu@123',email='sindhug@gmailcom',mobile='1234567890')
