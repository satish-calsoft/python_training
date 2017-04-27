#file1 = raw_input("Enter a filename to create for the data:")
#file2 = raw_input("Enter a filename to create for the copy operation")
#
#fopen1 = open(file1,"w")
#print dir(fopen1)
#
#str1 = raw_input("Enter text to copy::")
#
#
#fopen1.write(str1)
#fopen1.close()
#
#f3 = open(file1,"r")
#f4 = open(file2,"r+")
#
#str2 = f3.readlines()
#print type(str2)
#
#for i in str2:
#    f4.write(i)
#f3.close()
#f4.close()



#fp =open("file1.txt","r+")
#print  fp.read()
#print fp.tell()
#fp.seek(35)
#fp.write("krishna")
#fp.close()

fp = open("file1.txt","r")
st1 = raw_input("Enter a key to search and no.of occurences:")
str1 = fp.read()

j = 0
ind1 = 0 


sub1 =raw_input("Enter a substring to replace::")

fp.seek(0,0)
str1 = fp.read()
str1 =str1.split()

for it1 in range(len(str1)):
    if st1 == str1[it1]:
        str1[it1] = sub1
        j = j+1
    elif st1 in str1[it1]:
        print "%s exists in %s" %(st1,str1[it1])

print "count=",j
str1 = " ".join(str1)
print str1


#fp.seek(0,0)
#str1 = fp.readlines()
#line = 0
#for i in str1:
#    if st1 in i:
#        
#        ind1 = 0
#        x = i.count(st1)
#        print "x =",x
#        for j in range(x):
#            
#            ind1 = i.index(st1,ind1)
#            
#            print "line no :%d position::%d" %(line,ind1)
#            ind1 = ind1 + 1
#        line = line+1
        
    
fp.close()