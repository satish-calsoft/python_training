a="*"
b=int(raw_input("Enter a value::"))

i=1
s=""
l=b*2

for j in range(l):
    if j%2==0:
        continue
    elif j > 1 and j < (l-1) :
        s = a*l
        s = list(s)
        for i in range(len(s)):
            if i > 0 and i < len(s)-2:
                s[i] = " "
            elif i == len(s)-1:
                s[i] = " "
        s = "".join(s)
        print s
        
    else:
        s = a*l
        s = list(s)
        for i in range(len(s)):
            if i%2 !=0 :
                s[i]=" "  
        s="".join(s)
        print s        
            
  