# Remove the common element and print the whole list 
l1 = [1, 2, 4, 5, 7, 3]
l2 = [8, 1, 2, 5, 10, 11, 23]

l3 = []

for i in l1:
    if i not in l2: l3.append(i)

for i in l2:
    if i not in l1: l3.append(i)
    
print l3



################# Solution 2###########

l3 = l1 + l2

for i in l1 + l2:
    if i in l1 and i in l2:
        l3.remove(i)

print 'sol 2', l3

# List REVERSE functionality without in-build methods

l4 = l3
for i in range(len(l4)/2):
    l4[i], l4[-i - 1] = l4[-i - 1], l4[i]

print l4

# List POP functionality without in-build methods

inde = 2

if inde == None or inde == '':
    l4.remove(l4[-1])
else:
    l4.remove(l4[inde])
print l4
    

#Count Function
#l4 = 'test is test'
givenval = 11
cou = 0
for i in l4:
    if givenval == i:
        cou = cou + 1
print 'count', cou


#len function
length_of = 0
for i in l4:
    length_of = length_of + 1
print 'length of', length_of

## Prime numbers
innum = 50

def isprime(in_number):
    isprime_check = True
    for i in range(2, (in_number/2) + 1):
        if in_number % i == 0:
            isprime_check = False
    if isprime_check:
        return in_number

primelist = [2,]
for x in range(3, innum, 2):
    if isprime(x):
        primelist.append(x)
print primelist



#sort Function


