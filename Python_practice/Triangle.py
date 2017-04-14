#Triangle program
a="*"
b=int(raw_input("Enter a value"))
c=" "
i=1
s=""
l=b*2

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
        elif j==l-1:
            s=list(s)
            for i in range(len(s)):
                if i%2!=0:
                    s[i]=" "  
            s="".join(s)
            print s
        
        else:
            print s.center(l)
            
           


                    
                
        
    


    
    







    
  








