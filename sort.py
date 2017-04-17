#! /usr/bin/python
s = [8,7,6,4]
s1 = []
for i in range(len(s)):
    
       a = min(s)
       s1.append(a)
       s.remove(a)
print s1

