
import tableusingformat 


def validate_info():
    
    pass

def emp_info(list1,dict1):
    
    
    list2 = []
    sno = 1
    while 1:
        list2 = []
        h2 = raw_input("Press enter for the employee details or enter q to quit::")
        if h2 == "q":
            break
        elif h2 == "\n":
            pass
        else:
            list2.append(sno)
            for i in list1[1:]:
        
                h1 = raw_input("Enter %s::" %i)
                list2.append(h1)
    
                dict1[sno] = list2
        sno =  sno+1
    print dict1
    tableusingformat.table(dict1)      




def header_info():
    
    dict1 = {}
    list1 = []
    
    #while 1:
    #    
    #    h1 = raw_input("Ente the header or enter q to quit::")
    #    if h1 == "q":
    #        break
    #    elif h1 == "\n":
    #        pass        
    #    else:
    #        list1.append(h1)
    #dict1['a'] = list1
    list1 =["id","name","salary","mobile"]
    dict1['a'] = list1
    emp_info(list1,dict1)
        

header_info()
5