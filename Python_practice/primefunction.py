

def primefun(a):
 i = 0
 l1 = []
 for j in range(2,a+1):
     for l in range(1,j):
         if j%l==0 :
             i=i+1
     if i >= 2:
         pass
     else:
         l1 = l1+[j]
     i = 0
 return l1


a=int(raw_input("Enter a value::"))
l1 = primefun(a)
print "Prime numbers:",l1
