
f=open('replace.txt','w')
f.writelines('suseela is good girl she learned python very well\njyothi,sindu and suseela learned python suseela\n suseela ')
f.close()
f=open('replace.txt','r+')
fp=f.readlines()
print fp
s=raw_input('which word you want to replace:')
p=raw_input('which word you want to insert:')
f2=[]
for i in fp:
    f1=i.split()
    for j in f1:
        if j==s:      
            a=f1.index(s)
            f1.remove(j)
            f1.insert(a,p)
    print f1
    #f2.extend(f1)
    #print f2
#v=' '.join (f2)
    #print v
    fpp=open('replace.txt','a+')
    fpp.write('\n')
    fpp.writelines(f1)
    fpp.write('\n')
    fpp.close()     
  

    


    



    
