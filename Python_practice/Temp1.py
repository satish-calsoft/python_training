#var1="Hello world"
#print var1[:6]+'python'
#print var1

#for loops

# = [1,2,3,4,5]

#for k in i:
#    if k%2 == 0:
#        print "%d is even" %k
#    else:
#       print "%d is not even number" %k

#a=range(50)

#print a
#print 

#a=["*","*","*","*","*","*"]
#print a
#for i in range(len(a)):
#    if i%2!=0:
#        a[i]=" "
#    
#print a
#        
#        
#if :

#a=-1
#b=1
#
#if a>b:
#    print "Yes"
#else:
#    print "No"



#def sum(**args):
#    
#    print args
#    result = args['a']+args['b']+args['c']
#    print result
#    
#sum(a=1,b=2,c=3)


#s="asisai"
#i =0
#print s.index("s",i)
#i = s.index("s")
#print s.index("s",i+1)


#dict1 ={}
#j = 1
#
#while 1:
#    
#    d = raw_input("Do you want to continue::Press enter or press q to quit")
#    
#    if d == "q":
#        break
#    else:
#        name = raw_input("Enter name::")
#        id = raw_input("Enter id::")
#        dict1[id] =[name]
#        
#    
#print dict1

#list1="aaaaajjjjjjjjssssssaaaaaaaaaaaaaaaaaaaaaa"
#print "Given List is ",list1
#list2=""
#list3=[]
#ind = 0
#dict1={}
#
#
#for i in range(len(list1)):
#    
#    if i==len(list1)-1:
#        list2 = list2 +list1[i]
#        list3.append(list2)
#        
#        list2=""
#    else:
#        if list1[i]==list1[i+1]:
#            list2 = list2+list1[i]
#            
#        else:
#            list2 = list2+list1[i]
#            list3.append(list2)
#
#            list2=""
#print "Final List is",list3
#
#len_1 = 0
#index = 0
#for i in range(len(list3)):
#    
#    if len_1 < len(list3[i]):
#        len_1 = len(list3[i])
#        index = i
#    
#        
#    
#print len_1,index
#print list3[index]
    
    

#def f1():
#    def name(args):
#        print "NAME:",args
#    def age(args):
#        print "AGE:",args
#    def class1(args):
#        print "CLASS:",args    
#    
#    return name,age,class1
#
#fun = f1()
#print fun
#
#list1=["sai",23,7]
#for i in range(len(fun)):
#    fun[i](list1[i])
#



#def dec1(fun):
#    
#    def exc():
#        try:
#            return fun()
#        except Exception as e:
#            print e
#    return exc
#
#@dec1
#def f1():
#    a=10
#    print a
#    
#f1()



#def gen():
#    
#    for i in range(10):
#        yield i
#        
#k = gen()
#print k.next()
#print k.next()
#print dir(k)
#
#    
#l2 = xrange(10)
#print type(l2)
#
#for i in l2:
#    print i

k = input("Enter a number:")

for i in range(k+1):
    
    if i == k:
        while i != 0:
            
            l = "*"*i
            print l.rjust(20)  
            i = i-1   
    else:
        l = "*"*i
        print l.rjust(20)
