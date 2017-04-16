#'L.pop([index]) -> item -- remove and return item at index (default last).
#\nRaises IndexError if list is empty or index is out of range.'


l = [3,5,6,7,3,5,3,4,5,6,7]
l1 = []
j = 0
s = 0


for i in l:
    print "index %d,value %d" %(j,i)
    j = j+1
    

indval = int(raw_input("Enter the index value which is in range:: "))
if indval >= j:
    print "IndexError: pop index out of range"

#remove value 1 -> To remove this we need to skip this value while copying to another list

for i in range(len(l)):
    
    if i != indval:
        l1 = l1 + [l[i]]
    else :
        print "value",l[i]," deleted of index %d" %i
        
print "List::",l1
    
    