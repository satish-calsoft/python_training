#import exceptions,sys
#def div(a,b):
#    
#    raise Exception ("sai")
#    try:
#        result = float(a)/b
#        print result
#        print can
#        
#    except Exception as e:
#        sys.exit()
#        print e.message
#        
#     
#    finally:
#        print "sai"
#    #try:
#    #    print result
#    #except Exception as e:
#    #    print e.message
#    #    raise Exception ("result should defined")
#    #
#    #print result
#    print "python" 
#
#div(1,2)



#def readfile():
#    
#    try:
#        
#        f1 = open("sai1dsfsfsd.txt","r")
#        
#    except IOError as e:
#        print e
        
    
#def dict1():
#    
#    try:
#        d1 = {}
#        print d1["sai"]
#    except KeyError as e:
#        print e.message  
        
#readfile()
#dict1()

#import exceptionclass

#class Networkerror():
#    def __init__(self, arg):
#        self.args = arg


#class Networkerror(IndexError):
#    def __init__(self):
#        
#        #IndexError.__init__(self,"index out")
#        self.args = "index out"
#
#
#try:
#    #raise exceptionclass.Networkerror("Bad hostname")
#    d= [1,2,3]
#    print d[4]
#except  Networkerror as e:
#    print e

import sys

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
        
        
try:
    raise Networkerror("krishna")
    
except Networkerror as e:
    print e.args 
raise Exception('asdf')
print "sai"

