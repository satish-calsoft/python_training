#! /usr/bin/python
width = input("enter width")
height = input("enter the height of the triangle")
spaces = width
incr = 0

for i in range(width):
        
        spaces =spaces -1
        incr = incr+1
        print spaces*' '+incr*'*'.rjust(2)


        

                
                
