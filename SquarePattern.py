#!/usr/bin/python
a=raw_input("Enter the character: ")
width=4
height=4

for i in range(width/2):
    print a*width
    
    for j in range(height-2):
        print a*1+' '*(width-2)+a*1

        

    

    
