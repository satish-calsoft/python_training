###### for using str ##### c = '{0}  {1:^{z1}}  {2}'.format(j[0],j[1],j[2],z1= str(z))

a = {"keys":['S.no','Name','Mob.no'],"tar1":[11,"Double",9454234234],"tar2":[22,"kha",9983245344],"tar3":[33,"meeta",5674564312]}
b = 0
for j in a.values():
   # z=0
    c = '| {0}\t|{1:^5}\t| {2}\t|'.format(j[0],j[1],j[2]) 
    if len(c) > b:
        b = len(c) + 9
    #for i in range(len(c)):
        #if i>z:
            #z = i           
    d = '{0:-<{ln}}'.format('-',ln = b)   
    print d
  #  print '{0:>1}'.format('|')
    print c
print d

#print z