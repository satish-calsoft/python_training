#f=open('su.txt','w')
#f.writelines('suseela is good girl she learned python very well\njyothi,sindu and suseela learned python suseela\n suseela ')
#f.close()
f=open('su.txt','r+')
fp=f.readlines()
print fp
s=raw_input('which word you want to search:')
c=0

for i in fp:
    if i.endswith('.\n'):
        a=i.replace('.\n',' ')
        fp.remove(i)
        fp.append(a)

for i in fp:
    f1=i.split()
    print f1
    for j in f1:
        if s==j:
            c+=1
print c
    
    
