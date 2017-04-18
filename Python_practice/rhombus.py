#Rhombus
a="*"
b=int(raw_input("Enter a value::"))

i=1
s=""
l=b*2
t1 = []


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
            t1.append(s.center(l))
        elif len(s) == 1 :
            print a.center(l)
            t1.append(a.center(l))


a = -1

for i in t1:
    print t1[a]
    a  = a-1
       
              
                



    

            
           


                    
                
        
    


    
    







    
  








