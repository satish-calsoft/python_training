f=open('su.txt','w')
f.writelines('suseela is good girl she learned python very well \n jyothi and suseela learned python \n suseela hi hi.\n hi dahsdkjashjdlaksdj hdakjhdjs hi hi this suseela')
f.close()
f=open('su.txt','r+')
fp=f.readlines()
print fp
s=raw_input('which word you want to search in a file:')
c=0
for i in fp:
    if i.endswith('.\n'):
        a=i.replace('.\n',' ')
        fp.remove(i)
        fp.append(a)
#print fp
for i in fp:
    f1=i.split()
    #print f1
    for j in f1:
        if s==j:
            c+=1
print c
    
    
