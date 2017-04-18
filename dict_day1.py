l = range(10)
l1 = range(10,20)
dict = {}


#for i in range(len(l)):
    #dict[l[i]] = l1[i]
#print dict

########################
#l1 = range(10,15)

#for i in range(len(l)):
    #if i > len(l1) - 1:
        #dict[l[i]] = 'There is no value'
    #else:
        #dict[l[i]] = l1[i]
#print dict

###########################
#for i in range(1,20):
    #dict[i] = i ** 2

#print dict

###################
#key = 4
#dict.pop(key)
#print dict

####### Dict Sorting using Keys ##################
#dict = {4:8, 2:9}

#l4 = dict.keys()
#l5 = []
#l6 = [None] * len(l4)
#for i in range(len(l4)):
    #for j in l4:
        #if l4[i] < j:
            #l5.append('True')
        #else:
            #l5.append('False')
    #x = l5.count('False')
    #l6[x-1] = l4[i]
    #l5 = []
    
#for z in range(len(l6)):
    #if l6[z] == None:
        #l6[z] = l6[z+1]
    

#for i in l6:
    #print '({},{})'.format(i, dict[i])