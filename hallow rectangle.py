#!/usr/bin/python
size = input("enter size:")

print ('*' * (size+2))
for i in range(size-4):
    print ('*' + ' ' * (size) + '*')
print ('*' * (size+2))
