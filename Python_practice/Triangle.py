a="*"
b=int(raw_input("Enter a value"))
c=" "
i=1
s=""
l=b*2
#print a*l
#for j in range(l):
    #print c*(b-i),a
    #print c*(b+i),a
    #i=i+1
    #f=f-1
    #if i>b:break

for j in range(l):
    if j%2==0:
        continue
    else:
        s=a*j
        if len(s)>2 and j!=l-1:
            s=list(s)
            for i in range(len(s)):
                if i<(len(s)-1) and i!=0:
                    s[i]=" "            
            s="".join(s)
            print s.center(l)
       # elif j==l-1:
        #    s=list(s)
        #    i=0
        #    while i<l:
         #       if i!=0 and i<l-2:
         #           s[i]=" "
         #       i=i+1
         #   print "".join(s)
        else:
            print s.center(l)
            
           



                    
                
        
    


    
    







    
  








