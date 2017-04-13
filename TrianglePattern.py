#!/usr/bin/python
a=raw_input("Enter the character: ")

i=1
width=3
for i in range(width):
    i+=1
    
    print i
    print a.rjust(14-(i*3))*i
