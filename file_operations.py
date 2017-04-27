############# File Operations #######################
##########  Print line no and index of "word" #####################
#f = open("circle.py",'r') 
#a=f.read()
#spt = (" ","\n")
#for i in spt:
    #a = a.replace(i," ")
#c = a.split()
#print c.count("bob")
    
####### Working ##################

#f = open("circle.py","r")
#a = f.read()
#count=0
#for i in a.split():
    #if i == "bob":
        #count = count + 1
#print count
##########################Working 
f = open("circle.py","r")
a = f.readlines()
w = "bob"
line = 0
#y= len(a)
#print y
for i in a:
    if "bob" in i:
        x = i.count(w)
        ind = 0
        for j in range(x):
            ind = i.index(w,ind)
            print line,ind
    line = line + 1
#print z
        
######################
