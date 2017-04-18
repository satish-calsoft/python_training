#

i = [1,2,3,1,4,"s","s"]
print "List::",i
value=raw_input("Enter a value in the list to count:")
j = 0

for a in i:
    if str(a) == value:
        print value
        j = j+1

print "No.of occurences of %r:: %r" %(value,j)
    
   

    