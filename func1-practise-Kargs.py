def sum(**args):
    result = 0
    for v in args.values():
        result = result+v
    return result
    
print "result is", sum(a=3,b=2,c=3)
###########################3
#import pdb
def submit(**args):
    import pdb
    pdb.set_trace()
    result = 0
    for v in args.values():
        result = result+v
    return result
    
#print "result is", submit(user_name=ravi", l_name = "babu", passwd = "tehelka", mob_no=283982983, email = "abc@gmail.com")

#######Validations############