#! /usr/bin/python
inp = input("Enter input:")
sp = 1

for i in range(inp):
        if i == 0:
                print (' '*(inp))+' *'
        elif i<=inp-2:
                print ' '*((inp-i-1))+' *'+' '*i+'*'+' '*(i)+'*'
        elif i==inp-1:
                print (inp+1)*' *'
for j in range(inp,-1,-1):
        if j == 0:
                print ((' '*(inp))+' *')
        elif j<=inp-2:
                print ' '*((inp-j-1))+' *'+' '*j+'*'+' '*(j)+'*'
       
