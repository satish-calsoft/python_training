#This script is used to slicing strings

a = "PYTHON"
#P Y T H O N 
#0 1 2 3 4 5
-6 -5 -4 -3 -2 -1

b = a[:] #It display starting to end characters
print b 
c = a[::] #It also displays strating to end chars.
print c

print "To print only Y and H character" 
d = a[1:4:2]
print d 
print "To print only TH"
e = a[-4:-2]

n = raw_input("Enter a word: ")

print "We are going to revese the word oh!"

h = n[::-1]

print "The revesed string of %s is %s" % (n,h)





 
