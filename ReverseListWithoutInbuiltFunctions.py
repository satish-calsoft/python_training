#!/usr/bin/python

list1=[1,7,4,6,5,8]
#Reverse=[]
#Reverse=['','','','']
'''for i in range(0,4):
    for k in list1:
            i=i+0
print i'''
'''i=3
for j in range(4):
    Reverse[j]=list1[i-j]
    print Reverse
print Reverse '''

count=0
for k in list1:
    count=count+1
print count

for j in range(0,count/2):
    list1[j], list1[- j - 1] = list1[- j - 1], list1[j]
print list1
