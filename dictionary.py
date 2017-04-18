a = {"ntr":111,"anr":222}
a['robo']=333
print a 
######
a['robo'],a['bobo']=44,55
print a
##########
key=[0,1,2,3,4,5,6,7,8,9]
val=[10,11,12,13,14,15,16,17,18,19]
c={}
for i in range(len(key)):
    c[key[i]]=val[i]
print c
############squares##########3
d={}
for i in range(len(key)):
   d[i]=i*i
print "Squares", d
##############################
x=[1,2,3,4,5,6,7,8,9]
y=[10,11,12,13,14]
z={}
for i in range(len(x)):
    if i > (len(y)-1):
        z[x[i]]="no Value"
    else:
        z[x[i]]=y[i]
print z
