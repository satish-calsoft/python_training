
n=input("enter n: ")
count=0
def prime(n,count):
                if n==1:
                                print "prime number"
                else:
                                for i in range(1,n+1):
                                                if n%i==0:
                                                                count=count+1
                                                if count==2:                    
                                                                print "Prime number"
                                                else:
                                                                print "not a prime number"
prime(n,count)
    