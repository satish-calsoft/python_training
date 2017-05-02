###### for using str ##### c = '{0}  {1:^{z1}}  {2}'.format(j[0],j[1],j[2],z1= str(z))

a = {"keys":['S.no','Name','Mob.no'],"tar1":[11,"Ambuja",234234],"tar2":[22,"Maha",3245344],"tar3":[33,"Kcp",56745643]}
for j in a.values():
    z=0
    c = '{0}  {1:^10}  {2}'.format(j[0],j[1],j[2])
    
    #for i in range(len(c)):
        #if i>z:
            #z = i
    print '{0:-<25}'.format('-')
    print c
#print z