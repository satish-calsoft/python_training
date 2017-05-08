# list comphrensions

l1=[]
l1=[i for i in range(20)]
print l1

# if we want even num
l1=[i for i in range(20) if i %2==0]
print l1

d1={}

d1={i:j for i in range(20) for j in range(20) if i==j } 
print d1


