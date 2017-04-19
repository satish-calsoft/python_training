#l = [1,2,3,4,7,9,0]
#for i in l:
    ##print i
    #if i%2==0:
        #print i,"is an even number"
        
#print range(100)
#for i in range(101):
    #if i%2 == 0:
        #print i

#print range(0,100,2)
#print range(1,100,2)
#print range(0,-100,-2)

#print range(0,-101,-1)

#for loop
Odd_numbers = []
Even_numbers = []
for i in range(100):
    #Odd_numbers = [] # this will give empty list
    #Even_numbers = [] # this will give empty list    
    if i%2 == 1:
        #print i
        Odd_numbers.append(i)
    else:
        #print i
        Even_numbers.append(i)

print "Odd numbers are :", Odd_numbers
print "Even numbers are :", Even_numbers