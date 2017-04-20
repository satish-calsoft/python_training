lst=[1, 9, 8, 6, 1,2,5,3, 4]
for i in range(len(lst)):
            if i !=(len(lst)-1):
                        if lst[i]<=lst[i+1]:
                                    lst[i],lst[i+1]=lst[i+1],lst[i]
            
print lst
        
        
        
list1 = [-5, -23, 5, 0, 23, -6, 23, 67]
newlist = []

while list1:
            minimum = list1[0]  # arbitrary number in list 
            for x in list1: 
                        if x < minimum:
                                    minimum = x
            newlist.append(minimum)
            list1.remove(minimum)    

print newlist

####################

string='cat'
n="tac"
count=0
if len(string)==len(n):
            for i in string:
                        if i in n:
                                    print i,"in n"
                                    print count
                                    count=count+1
                        if i in n:
                                    count=count+1
                        if i in n:
                                    count=count+1
            print count

if count<=len(n):
            print "yes"
        