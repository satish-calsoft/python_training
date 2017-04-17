def prime(n):
    #n=input("enter n: ")
    count=0
    if n==1:
        print n
    else:
        for i in range(1,n+1):
            if n%i==0:
                count=count+1
        if count==2:
            print n
        #else:
         #   print "not a prime number"

for j in range(1,51):
    prime(j)