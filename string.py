#String operations

name = "my name is Devender"
#Buid-in string methods
#Capitalize - > 
#name.capitalize()
capitalize = name.capitalize()
print capitalize
#Center ->
center = name.center(35, 'd')
print center
#Count ->
count = name.count('e',0,len(name))
print count 
#encode ->
encode = name.encode('base64', 'strict')
print encode
#decode
decode = name.decode()
print decode
#endswith
endswith = name.endswith('r', 0, 40)
print endswith
#find 
find = name.find('e',0, 33)
no_find = name.find('w',0, 33)
print find
print no_find

#Index
index = name.index('v', 0, 22)
#no_index = name.index('z', 0, 22)
print index
#print no_index

#isalpha
isalpha = name.isalpha()
print isalpha
#isdigit
isdigit=name.isdigit()
print isdigit
#islower
islower = name.islower()
print name.islower() 
#isspace
isspace = name.isspace()
#istitle
istitle = name.istitle()
print name.istitle()
#isupper
isupper = name.isupper()
print name.isupper() 
#len
print name 
len = len(name)
print len

#ljust 
ljust = name.ljust(100, 'd')
print name.ljust(100, 'd')
#upper
upper = name.upper() 
print upper

#lower
lower = upper.lower()
print lower
#max
max = max(name)
print max 

#min 
min = min(name)
print min 

#replace
name.replace('is', 'was')

#rfind -> Same as find(), but search backwards in string. -->rfind(str, beg=0,end=len(string))

#rindex -> rindex( str, beg=0, end=len(string)) --> Same as index(), but search backwards in string.

#rjust

rjust = name.rjust(100, '#')

print rjust

#rstrip

#split

split = name.split()
print split

#strip

str = "0000000this is string example....wow!!!0000000";
str.strip('0')

#swapcase
swapcase = name.swapcase()
print swapcase

print "String operations"



 
 




