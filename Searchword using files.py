fp=open("f1.txt","w")
fp.writelines("test jyo\n jyo jyo \n python \n jyo  jyo python\n python \n test \n")
fp.close()
fr=open("f1.txt","r")
fi= fr.readlines()
print fi
I = raw_input("Enter the word you want to search")


'''N=fi.count(I)
    
print N '''
c=0

for  i in fi:
    # i
   
    s = i.split()
    print s
    for j in s:
        if j ==I:
             
            c+=1
print c


