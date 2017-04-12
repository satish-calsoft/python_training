



"""
Below are the methods of String Class: 
-----------------------------------------
capitalize
center
count
decode
encode
endswith
expandtabs
find
format
index
isalnum
isalpha
isdigit
islower
isspace
istitle
isupper
join
ljust
lower
lstrip
partition
replace
rfind
rindex
rjust
rpartition
rsplit
rstrip
split
splitlines
startswith
strip
swapcase
title
translate
upper
zfill
"""

#DAY-2


#String Slicing


print "\n\n#########The below OUTPUT is from String Slicing practice#####################\n\n"
name = "Hello world"


sliced_name = name[0:5]

print "sliced from [0:5] 'hello world': ", sliced_name
print "sliced to print only world: ", name[6:11]
print "sliced to print every third letter from the begining: ", name[::3]
print "sliced to print od: ", name[7::3]
print "sliced to print or: ", name[4::4]
print "reversed the string through slicing: ", name [::-1]
print "sliced to print substring of an sliced output 's[::2][:3:]': ", name[::2][:3:]

# From here LIST coding starts

print "\n\n##################The below OUTPUT is from LIST coding ##############\n\n"



l = [1,2,3]


l.reverse() #this will reverse the list in place(does not return anything)
l.append([4,5]) #this will append to the end of the list and does not return anything
print l.count(3) #this will cound the occurences of the value 3 in the given list
l.remove(3) #this will remove the first occurence of the value from the list

l2 = "abc"
print l.extend(l2) # this will append the elements from the iterable like [1,2,3,'a','b','c']

print l.pop() # this will remove element at the index from the list (by default last element) and returns a value as well.

l.sort()

l.index(2) # this will 
print l

# TASK - Do a calculation program 



# DAY-3



















