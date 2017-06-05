a = [1,2,3,[4,5],6,[7,8,9]]
b = ["a","b","c","d","e","f","g","h","i"]
a1 = a
k = 0
i = 0
while i != len(b):
    
    if isinstance(a1[k],int):
        a1[k] = b[i]
        k = k+1
        i = i+1
    else:
        
        for f in range(len(a1[k])):
            a1[k][f] = b[i]
            i = i+1
      
        k = k+1
        
            
       
print a1

            