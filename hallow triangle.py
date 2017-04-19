#! /usr/bin/python
inp = input("Enter input:")

for i in range(inp):
        if i == 0:
                print ((' '*(inp))+' *')
        elif i<=inp-2:
                print (' '*((inp-i-1))+' *'+' '*(2*i)+' *'+' '*(inp-i-1))
        elif i==inp-1:
                print (inp+1)*' *'
                
                
                
