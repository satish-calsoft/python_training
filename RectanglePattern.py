#!/usr/bin/python
width=input("Enter the width range: ")
x=raw_input("Enter the character: ")
print (x+' ')*(width+4)
for i in range(0,width):
    print x+('  ')*(width+2)+(' '+x)
print (x+' ')*(width+4)
