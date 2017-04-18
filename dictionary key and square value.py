# display dictionary by applying key=value*value formala by given range. 
a=input("enter range:")
d={}
for i in range(1,a+1):
    d.update({i:i**2})
print d