a="*"
b=int(raw_input("Enter length::"))
p=int(raw_input("Enter breadth::"))

i=1
s=""
l=b*2
z=p*2
for j in range(z):
    if j%2==0:
        continue
    elif j > 1 and j < z-1:
        s = a*l
        s = list(s)
        for i in range(len(s)):
            if i > 0 and i < len(s)-2:
                s[i]=" "
            elif i == len(s)-1:
                s[i] = " "            
        s="".join(s)
        print s              
        
    else:
        s = a*l
        s = list(s)
        for i in range(len(s)):
            if i%2 !=0 :
                s[i]=" "  
        s="".join(s)
        print s        
            
