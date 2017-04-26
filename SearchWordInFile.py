'''fp=open("Search.txt",'w')
for i in range(15):
    fp.writelines('This is python learning program\n')
fp.close()

fr=open("Search.txt",'r')
#count=0

fs=fr.read()
a=fs.count('python')
#count=count+a
    
#print count
print a'''

#fp=open("Search.txt",'w')
#for i in range(15):
#    fp.writelines('This is python learning program\n')
#fp.close()

count=0
fr=open("Search.txt",'r')
a=fr.readlines()
b=raw_input("Enter the search word: ")
for i in a:
    c=i.split()
    #print c
    for j in c:
        if b==j:
            #print b
            count=count+1
            #print count
print count
        
    
