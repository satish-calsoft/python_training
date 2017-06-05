
import K

dict1 ={"keys":["NAME","ID","MOBILE","DESC"],"emp1":["sai","10","9676083138","QE"],"emp2":["krishna chaitanya vemuri sdhfksdfhj sai","20","9676083138","QE"],"emp3":["chaitanya","30","9676083138","QE"]}





def table(dict1):
    g1 = 0 
    #Returns the highest length in the name
    for i in dict1.values():
        
        if len(i[1]) > g1:
            g1 = len(i[1])
    
    #First line    
    for j in i:
        if j == i[1]:
            
            print "+",'{:-<{g}}'.format("-",g=str(g1)),
            
        else:
            print "+",'{:-<10}'.format("-"),
    print "+"
    
    for f,i in dict1.items():
          
        
        for j in i:
            if j == i[1]:
                
                print "|",'{:<{g}}'.format(j,g=str(g1)),
                
            else:
                print "|",'{:<10}'.format(j),
        print "|"
        
        for j in i:
            if j == i[1]:
                
                print "+",'{:-<{g}}'.format("-",g=str(g1)),
                
            else:
                print "+",'{:-<10}'.format("-"),
        print "+"
    
def _table1():
    
    print "sai"