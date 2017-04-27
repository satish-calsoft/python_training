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

#in fp.read we can give no.of characters to read
#print str1
str1 =str1.split()
print str1

j = 0

str2 =""

for i in str1:
    
    if i == st1:
        j = j+1
    elif st1 in i :
        print i
print "count is:",j




fp.seek(0,0)
str1 = fp.readlines()


ind1 = 0 
j = 0
for i in range(len(str1)):
    if st1 in str1[i]:
        
        print "line number=%d" %i   
        x = str1[i].count(st1)
        for j in range(x):
            
            ind1 =str1[i].index(st1,ind1)
            print "position::",ind1
            ind1 = ind1+1
        
fp.close()







