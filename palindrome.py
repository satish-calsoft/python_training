# Palindrome program
a=raw_input("enter value or string: ")
l=[]
l1=[]
l2=[]
for i in a:
    l.append(i)
#print l
l1=l
x=''.join(l1)
x1=x.lower()
l.reverse()
l2=l
y=''.join(l2)
y1=y.lower()
if x1==y1:
    print 'its a palindrome'
else:
    print 'not a palindrome'
    
    

    