########### Working using module #################
import string
with open("circle.py","r+") as f:
    a = f.read()
    #b = string.replace(a, 'bob', 'job')
#print b

############################ worked without using replace #####
    b = a.split()
    for i in b:
        if i == "bob":
            j = b.index(i)
            b.pop(j)
            b.insert(j, "job")
    print b
    #f.seek(0)
    #for i in b:
        #f.write(i)
    #f.seek(0)
    #print f.read()
  # print a = a.split("bob")
################################  
   # spt = (" ","\n")
    #for i in spt:
        #a = a.replace(i," ")
    #c = a.split()
    #for j in c:
        #if j == "bob":
            #c = c.
        #if "bob" in i:
            #y = a.replace("bob", "job")
#    print y
        