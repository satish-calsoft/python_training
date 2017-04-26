count=0
inpt='is'
f=open("f1.txt",'r')
s=f.readlines()
for i in s:
    l=i.split()
    for j in l:
        if inpt.lower() in j.lower():
            count=count+1
f.close()
print count