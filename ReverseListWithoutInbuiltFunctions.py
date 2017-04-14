#!/usr/bin/python

list1=[1,7,4,6]
Reverse=['','','','']
'''for i in range(0,4):
    for k in list1:
            i=i+0
print i'''
i=3
for j in range(0,4):
    Reverse[j]=list1[i-j]
print Reverse 
