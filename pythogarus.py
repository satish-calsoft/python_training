# a^2 + b^2 =c^2
# 3^2 + 4^2 = 5^2   9 + 16 = 25
#list=[]
"""for i in range(50):
    j=i+1
    k=i+2
    l=[]
    flag=0
   # print "{} {} {}".format(i,j,k)
    if i*i + j*j != k*k:
        print "ijk"
        flag=1
    if flag==1:
        l=[i,j,k]
    print l"""

for i in range(1,50):
    for j in range(1,50):
        for k in range(1,50):
           if i*i + j*j == k*k:
               #print "ijk"
               flag=1
               if flag==1:
                   l=[i,j,k]
                   print l