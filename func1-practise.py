def sum(**args):
    result = 0
    for v in args.values():
        result = result+v
    return result
    
print "result is", sum(a=3,b=2,c=3)
###########################3
def submit(**args):
    result = 0
    for v in args.values():
        result = result+v
    return result
    
print "result is", submit(user_name="ravi",l_name="babu",mob_no="283982983")