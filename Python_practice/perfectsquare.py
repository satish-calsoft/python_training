
#a2+b2=c2
int1=int(raw_input("Enter a range::"))

for i in range(1,int1):
    for j in range(1,int1):
        for k in range(1,int1):
            if i*i+j*j == k*k and i<j<k:
                print i,j,k
    